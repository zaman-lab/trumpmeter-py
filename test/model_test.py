import os

from keras.engine.training import Model

from app.model import unweighted_model, weighted_model, saved_model, MODEL_FILEPATH, WEIGHTS_FILEPATH

def test_filepaths():
    assert os.path.isfile(MODEL_FILEPATH)
    assert os.path.isfile(WEIGHTS_FILEPATH)

def test_unweighted_model():
    assert isinstance(unweighted_model(), Model)

def test_weighted_model():
    assert isinstance(weighted_model(), Model)

def test_saved_model():
    assert isinstance(saved_model(), Model)
