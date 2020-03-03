import os
import logging
import sys

from operator import itemgetter

from flask import Flask, redirect, request, session
from flask.logging import create_logger
from pyga.requests import Tracker, Page, Session, Visitor
from pyga import utils
from urllib.parse import urlparse
from urllib.error import URLError

app = Flask(__name__)
logger = create_logger(app)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    logger.handlers = gunicorn_logger.handlers
    logger.setLevel(gunicorn_logger.level)


redirect_type = int(os.environ.get('REDIRECT_TYPE', '302'))
redirect_target = os.environ.get(
    'REDIRECT_TARGET', 'https://www.pioneera.com/')
google_analytics = os.environ.get('GA', None)
listening_port = int(os.environ.get('PORT', 8080))

logger.info('Adding redirection handling to target %s with code %d',
            redirect_target, redirect_type)

if google_analytics:
    logger.info('Logging to Google Analytics as %s',
                google_analytics)


def log_traffic(request):
    if not google_analytics:
        return
    url = urlparse(request.base_url)

    pyga_tracker = Tracker(google_analytics, url.hostname)

    pyga_visitor = Visitor()
    pyga_visitor.ip_address = request.access_route[0]
    pyga_visitor.user_agent = request.headers.get('User-Agent')
    user_locals = []
    if 'Accept-Language' in request.headers:
        al = request.headers.get('Accept-Language')
        if al is not None:
            matched_locales = utils.validate_locale(al)
            if matched_locales:
                lang_lst = map((lambda x: x.replace('-', '_')),
                               (i[1] for i in matched_locales))
                quality_lst = map((lambda x: x and x or 1),
                                  (float(i[4] and i[4] or '0')
                                   for i in matched_locales))
                lang_quality_map = map((lambda x, y: (x, y)),
                                       lang_lst, quality_lst)
                user_locals = [x[0] for x in sorted(
                    lang_quality_map, key=itemgetter(1), reverse=True)]
    if user_locals:
        pyga_visitor.locale = user_locals[0]

    pyga_session = Session()

    pyga_page = Page(url.path)
    pyga_page.referrer = request.headers.get('Referer')

    logger.info(
        'Logging GA traffic from %s to host %s with page %s', pyga_visitor.ip_address, url.hostname, url.path)

    try:
        pyga_tracker.track_pageview(pyga_page, pyga_session, pyga_visitor)
    except URLError:
        logger.warn('Unable to connect to analytics')
    except:
        logger.error('Analytics logging failed')
        logger.error(sys.exc_info())


@app.route('/')
def root():
    log_traffic(request)
    return redirect(redirect_target, code=redirect_type)


@app.route('/<path:page>')
def anypage(page):
    log_traffic(request)
    return redirect('{new_url}#{page}'.format(page=page, new_url=redirect_target), code=redirect_type)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=listening_port)
