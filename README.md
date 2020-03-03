<h1  align="center">Welcome to web-redirect 👋</h1>
<p>
<img  alt="Version"  src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000"  />
<a  href="http://www.apache.org/licenses/LICENSE-2.0"  target="_blank">
<img  alt="License: APACHE--2"  src="https://img.shields.io/badge/License-APACHE--2-yellow.svg"  />
</a>
<a  href="https://twitter.com/troykelly"  target="_blank">
<img  alt="Twitter: troykelly"  src="https://img.shields.io/twitter/follow/troykelly.svg?style=social"  />
</a>
</p>

> Receive RouterOS DHCP Lease events and update a DNS server

### 🏠 [Homepage](https://github.com/Pioneera/web-redirect)

## Assumptions

You have a Google Cloud account, you have enabled billing and Google Cloud Run. (If you are hosting this in Cloud Run)

## Usage

If you just want to deploy and get running - copy `.env.example` to `.env` and update the information.

Once that is up-to-date - just run `./deploy.sh` and your project will be deployed

## Configuration

### .env example

```text
PROVIDER: constellix
CONSTELLIX_USERNAME: d0ff4ace-e47a-4c27-af93-744c553cf4d5
CONSTELLIX_TOKEN: cc87ef6e-4322-48f0-8865-e6618c7bbd0a
SERVICE_NAME=service-name
REGION=australia-southeast1
PROJECT_ID=project-id
```

| Variable              | Required | Note                                                        |
| --------------------- | -------- | ----------------------------------------------------------- |
| `SERVICE_NAME`        | No       | Cloud Run service name (only needed if using `./deploy.sh`) |
| `REGION`              | No       | Cloud Run region (only needed if using `./deploy.sh`)       |
| `PROJECT_ID`          | No       | Cloud Run project ID (only needed if using `./deploy.sh`)   |
| `PROVIDER`            | Yes      | Currently only `CONSTELLIX` supported                       |
| `CONSTELLIX_USERNAME` | Yes      | The Constellix API username                                 |
| `CONSTELLIX_TOKEN`    | Yes      | The Constellix API password                                 |

## Author

👤 **Troy Kelly**

- Website: http://troykelly.com/
- Keybase: [@troykelly](https://keybase.io/troykelly)
- Twitter: [@troykelly](https://twitter.com/troykelly)
- Github: [@troykelly](https://github.com/troykelly)
- LinkedIn: [@troykelly](https://linkedin.com/in/troykelly)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br  />Feel free to check [issues page](https://github.com/Aperim/routeros-constellix-gateway/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Aperim Pty Ltd](https://github.com/Aperim).<br  />
This project is [APACHE--2](http://www.apache.org/licenses/LICENSE-2.0) licensed.

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
