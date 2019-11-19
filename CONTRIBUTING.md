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

To classify text, this app needs access to the model's final weights file, which we're hosting on a publicly-available Google Cloud Storage bucket called ["trumpmeter-bucket"](https://console.cloud.google.com/storage/browser/trumpmeter-bucket/).

Download the final model weights file (`gs://trumpmeter-bucket/model/weights/weights-reconstructed.hdf5`) and move it into the local "model/weights" directory.

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
