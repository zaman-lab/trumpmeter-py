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


## Usage

### CLI

Run the classifier via a command-line client, where you'll have the opportunity to classify your own user-provided text:

```sh
python -m app.client
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
