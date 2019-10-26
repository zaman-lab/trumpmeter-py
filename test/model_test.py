import os

from keras.engine.training import Model

from app.model import unweighted_model, original_model, final_model, MODEL_FILEPATH, WEIGHTS_FILEPATH

def test_filepaths():
    assert os.path.isfile(MODEL_FILEPATH)
    assert os.path.isfile(WEIGHTS_FILEPATH)

def test_unweighted_model():
    assert isinstance(unweighted_model(), Model)

def test_original_model():
    assert isinstance(original_model(), Model)

def test_final_model():
    assert isinstance(final_model(), Model)
