

import os

import pandas

DATA_DIRPATH = os.path.join(os.path.dirname(__file__), "..", "model", "data")

def test_labeled_data():
    LABELED_TWEETS_CSV_FILEPATH = os.path.join(DATA_DIRPATH, "labeled_data_balanced.csv")
    df = pandas.read_csv(LABELED_TWEETS_CSV_FILEPATH)
    assert len(df) == 1_100_000
    assert df.columns.tolist() == ['Unnamed: 0', 'tweet', 'rep/dem']

def test_labeled_data_truncated():
    LABELED_TWEETS_CSV_FILEPATH = os.path.join(DATA_DIRPATH, "labeled_data_balanced_Trump_100k.csv")
    df = pandas.read_csv(LABELED_TWEETS_CSV_FILEPATH)
    assert len(df) == 220_000
    assert df.columns.tolist() == ['Unnamed: 0', 'tweet', 'rep/dem']
