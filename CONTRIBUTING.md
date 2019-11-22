# Contributor's Guide

Hey, so you want to run this app yourself? Great. Follow the instructions in this guide.

## Installation

Create and activate a virtual environment, using anaconda for example, if you like that kind of thing:

```sh
conda create -n trumpmeter-env python=3.7 # (first time only)
conda activate trumpmeter-env
```

Install package dependencies:

```sh
pip install -r requirements.txt # (first time only)
```

### Model File Storage

To classify text, this app needs access to certain model-related files, which we're hosting on a publicly-available Google Cloud Storage bucket called ["trumpmeter-bucket"](https://console.cloud.google.com/storage/browser/trumpmeter-bucket/).

  + `gs://trumpmeter-bucket/model/weights/weights-reconstructed.hdf5`
  + `gs://trumpmeter-bucket/model/dictionaries`

Feel free to use the files in this bucket (i.e. "remote" storage option), or download them into your local repository for faster file-load times (i.e. "local" storage option). Depending on which storage option you choose ("local" or "remote"), set the environment variable `STORAGE_ENV` accordingly. If choosing the "remote" storage option: download your Google Cloud API service account credentials and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable accordingly.

After configuring your storage option, run the storage service to verify all files are in place:

```sh
python -m app.storage_service
# OR
STORAGE_ENV="local" python -m app.storage_service
# OR
STORAGE_ENV="remote" python -m app.storage_service
```

### Twitter Bot Setup

Create a [Twitter account](https://twitter.com/) with a handle like ["@trumpmeter_bot"](https://twitter.com/trumpmeter_bot), and set the `TWITTER_BOT_HANDLE` environment variable accordingly.

Obtain credentials for your own [Twitter app](https://developer.twitter.com/) with access to the Twitter API, and set the environment variables `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN`, and `TWITTER_ACCESS_TOKEN_SECRET` accordingly.

## Usage

### CLI

Run the classifier via a command-line client, where you'll have the opportunity to classify your own user-provided text:

```sh
python -m app.client
```

### Twitter Bot

Run the classifier via a Twitter Bot, which will reply to at-mentions with the predicted pro-Trump score polarity score:

```sh
python -m app.bot
```

## Testing

Install pytest:

```sh
pip install pytest # (first time only)
```

Run tests:

```sh
pytest --disable-pytest-warnings
```


## Deploying

Create a new app server (first time only):

```sh
heroku create trumpmeter-bot # (use your own app name here)
```

Provision and configure the Google Application Credentials Buildpack to generate a credentials file on the server:

```sh
heroku buildpacks:add https://github.com/elishaterada/heroku-google-application-credentials-buildpack
heroku config:set GOOGLE_CREDENTIALS="$(< google-credentials.json)"
heroku config:set GOOGLE_APPLICATION_CREDENTIALS="google-credentials.json"
```

Configure the rest of the environment variables:

```sh
heroku config:set APP_ENV="production"
heroku config:set STORAGE_ENV="remote"
# etc...
heroku config:set TWITTER_BOT_HANDLE="@trumpmeter_bot"
heroku config:set TWITTER_CONSUMER_KEY="____"
heroku config:set TWITTER_CONSUMER_SECRET="____"
heroku config:set TWITTER_ACCESS_TOKEN="____-____"
heroku config:set TWITTER_ACCESS_TOKEN_SECRET="____"
```

Deploy:

```sh
# from master branch
git checkout master
git push heroku master

# or from another branch
git checkout mybranch
git push heroku mybranch:master
```

Test everything is working in production:

```sh
heroku run "python -m app.storage_service"
heroku run "python -m app.dictionaries"
heroku run "python -m app.client"
```

Run the bot in production, manually:

```sh
heroku run "python -m app.bot"
```

... though ultimately you'll want to setup a Heroku "dyno" to run the bot as a background process (see the "Procfile"):

```sh
heroku ps:resize bot=standard-2x
```

Checking logs:

```sh
heroku logs --ps bot
```
