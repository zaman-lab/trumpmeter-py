
from pprint import pprint
import os

from conftest import EXAMPLE_TWEETS
from app.model import reconstructed_final_model
from app.helper_text import main_clean

def classify(txt, model):
    """
	Params:
		txt is the text to classify
		model is the model used to perform the classification
	"""
    x, x_s = main_clean(txt)
    results = model.predict([x, x_s])
    results = results[0]
    #return {"text": txt, "pro_trump": results[0], "other_num": results[1]} # not really sure if these are correct assignments
    return {"text": txt, "pro_trump": results[0], "temp": [round(float(score), 4) for score in results] }

if __name__ == "__main__":

    model = reconstructed_final_model()

    for twt in EXAMPLE_TWEETS:
        print("\n-----------------------------")
        print(f"TWEET: '{twt}'")
        response = classify(twt, model)
        print("CLASSIFICATION:", response["temp"])

    while True:
        user_text = input("Your Text (press ENTER at any time to quit): ")
        if user_text in ["", "exit", "exit()"]: break
        results = classify(user_text, model)
        pprint(results)
        print("-----------------------------")
