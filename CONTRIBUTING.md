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

## Usage

### CLI

Run the classifier via a command-line client, where you'll have the opportunity to classify your own user-provided text:

```sh
python -m app.client
```
