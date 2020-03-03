#!/usr/bin/env bash

# From https://gist.github.com/judy2k/7656bfe3b322d669ef75364a46327836#gistcomment-2952096
read_var() {
  if [ -z "$1" ]; then
    echo "environment variable name is required"
    return
  fi

  local ENV_FILE='.env'
  if [ ! -z "$2" ]; then
    ENV_FILE="$2"
  fi

  local VAR=$(grep $1 "$ENV_FILE" | xargs)
  IFS="=" read -ra VAR <<< "$VAR"
  echo ${VAR[1]}
}

TS=$(date +%s%N | cut -b1-13)

echo "Enabling Cloud Build and Cloud Run in $(read_var PROJECT_ID)"
gcloud services enable --project=$(read_var PROJECT_ID) cloudbuild.googleapis.com run.googleapis.com

echo "Submitting $(read_var SERVICE_NAME) build in $(read_var PROJECT_ID)"
gcloud builds submit --config=cloudbuild.yaml \
    --project=$(read_var PROJECT_ID) \
    --substitutions=_SERVICE_NAME=$(read_var SERVICE_NAME),_REGION=$(read_var REGION),_REDIRECT_TYPE=$(read_var REDIRECT_TYPE),_REDIRECT_TARGET=$(read_var REDIRECT_TARGET),_GA=$(read_var GA),COMMIT_SHA=manual${TS} \
    .