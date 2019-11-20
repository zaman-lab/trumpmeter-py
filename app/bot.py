
from app.model import reconstructed_final_model
from app.classifier_model import ClassifierModel

from polarity_bot.stream import stream

if __name__ == "__main__":
    #print("APP ENV", APP_ENV)

    model = ClassiModeModelfierModel(model=reconstructed_final_model())

    stream = stdout_stream(model)
    stream.filter(track=[BOT_HANDLE])

    # this never gets reached
