import os

from keras.engine.training import Model

from app.model import (
    ORIGINAL_WEIGHTS_FILEPATH, FINAL_MODEL_FILEPATH, FINAL_WEIGHTS_FILEPATH,
    unweighted_model, original_model,
    saved_final_model, reconstructed_final_model, production_model
)

def test_filepaths():
    assert os.path.isfile(ORIGINAL_WEIGHTS_FILEPATH)
    assert os.path.isfile(FINAL_MODEL_FILEPATH)
    assert os.path.isfile(FINAL_WEIGHTS_FILEPATH)

def test_unweighted_model():
    assert isinstance(unweighted_model(), Model)

def test_original_model():
    assert isinstance(original_model(), Model)

def test_saved_final_model():
    assert isinstance(saved_final_model(), Model)

def test_reconstructed_final_model():
    assert isinstance(reconstructed_final_model(), Model)

def test_production_model():
    assert isinstance(production_model(), Model)
