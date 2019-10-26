
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

    orig_model = original_model()
    model = final_model()

    twt = "He is awesome, make american great again. Democrats is taking off. We love democrats."
    r1 = classify(twt, orig_model)
    pprint(r1)
    print("-----------------------------")
    r2 = classify(twt, model)
    pprint(r2)
    print("-----------------------------")

    twt2 = "Trump for President!!! #MAGA"
    r3 = classify(twt2, orig_model)
    pprint(r3)
    print("-----------------------------")
    r3 = classify(twt2, model)
    pprint(r3)
    print("-----------------------------")

    while True:
        user_text = input("Your Text (press ENTER at any time to quit): ")
        if user_text in ["", "exit", "exit()"]: break
        results = classify(user_text, model)
        pprint(results)
        print("-----------------------------")
