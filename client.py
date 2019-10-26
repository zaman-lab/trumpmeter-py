

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
	results = model.predict([x, x_s]) #> array([[0.57155126, 0.42844874]], dtype=float32)
	results = results[0] #> array([0.57155126, 0.42844874], dtype=float32)
	response = {"text": txt, "pro_brexit": results[1]}
	return response

def test_classify():
    #model = weighted_model()
    model = final_model()
    #print(model.summary())
    print("MODEL:", type(model))

    txt = "He is awesome, make american great again. Democrats is taking off. We love democrats."
    print("EXAMPLE TWEET:", txt)

    model_len = 20 # ???
    x, x_s = main_clean(txt, model_len)

    prediction = model.predict([x, x_s])
    #> ORIGINAL array([[0.15433621, 0.84566385]], dtype=float32)
    #> FINAL array([[0.01033916, 0.98966086]], dtype=float32)
    prediction = prediction[0]
    pro_pol = prediction[0]
    print("PRO-TRUMP SCORE:", pro_pol)
    #> ORIGINAL 0.15433621
    #> FINAL 0.010339164
    return {"text": txt, "pro_trump": pro_pol}


if __name__ == "__main__":

    test_classify()




	#model = load_model()
    #while True:
    #    user_text = input("Your Text (press ENTER at any time to quit): ")
    #    if user_text in ["", "exit", "exit()"]: break
    #    results = classify(user_text, model)
    #    print(results)
