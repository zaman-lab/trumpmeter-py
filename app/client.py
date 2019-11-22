
from pprint import pprint
import os

from conftest import EXAMPLE_TWEETS
from app import APP_ENV
from app.model import production_model #reconstructed_final_model
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
    #return {"text": txt, "pro_trump": results[0], "temp": [round(float(score), 4) for score in results] } # pro-trump appears to be the second number
    pro_score = round(float(results[1]), 4)
    #pro_score = results[1]
    return {"text": txt, "pro_trump": pro_score}

if __name__ == "__main__":

    model = production_model() # reconstructed_final_model()

    for twt in EXAMPLE_TWEETS:
        print("\n-----------------------------")
        print(f"TWEET: '{twt}'")
        response = classify(twt, model)
        print("CLASSIFICATION:", response["pro_trump"])

    if APP_ENV != "production":
        while True:
            user_text = input("Your Text (press ENTER at any time to quit): ")
            if user_text in ["", "exit", "exit()"]: break
            results = classify(user_text, model)
            pprint(results)
            print("-----------------------------")
