
from pprint import pprint
import os

from model import original_model, final_model
from helper_text import main_clean

def classify(txt, model):
    """
	Params:
		txt is the text to classify
		model is the model used to perform the classification
	"""
    x, x_s = main_clean(txt)
    results = model.predict([x, x_s])
    results = results[0]
    #return {"text": txt, "pro_trump": results[1]}
    return {"text": txt, "results": results}

if __name__ == "__main__":

    model_o = original_model()
    model_f = final_model()

    example_tweets = [
        "Trump for President!!! #MAGA",
        "Trump is the best ever!",
        "If Clinton is elected, I'm moving to Canada",

        "He is awesome, make american great again. Democrats is taking off. We love democrats.",

        "Hillary for President!!! #StrongerTogether",
        "Trump is the worst ever!",
        "If Trump is elected, I'm moving to Canada",
    ]

    for twt in example_tweets:
        print("-----------------------------")
        print(f"TWEET: '{twt}'")
        #print("-----")
        #print("ORIGINAL MODEL SAYS...")
        response_o = classify(twt, model_o)
        print("ORIG:", response_o["results"])
        #print("-----")
        #print("FINAL MODEL SAYS...")
        response_f = classify(twt, model_f)
        print("FINAL:", response_f["results"])

    exit()

    model = model_o
    while True:
        user_text = input("Your Text (press ENTER at any time to quit): ")
        if user_text in ["", "exit", "exit()"]: break
        results = classify(user_text, model)
        pprint(results)
        print("-----------------------------")
