
import os

from app.model import saved_model, unweighted_model

RECONSTRUCTED_WEIGHTS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "model", "weights", "weights-reconstructed.hdf5")

def recreate_weights(weights_filepath):
    fm = saved_model()
    fm.save_weights(weights_filepath)

def reconstructed_model(idempotent=True):
    if idempotent == False:
        recreate_weights(RECONSTRUCTED_WEIGHTS_FILEPATH)
    rm = unweighted_model()
    rm.load_weights(RECONSTRUCTED_WEIGHTS_FILEPATH)
    return rm

if __name__ == "__main__":

    fm = saved_model()
    # had some issues uploading the final model to GCS, but maybe the weights file is uploadable...
    rm = reconstructed_model(idempotent=False)
