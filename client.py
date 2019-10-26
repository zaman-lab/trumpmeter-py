

import os

from model import load_model
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

    model = load_model()
    print(model.summary())

    twt = "He is awesome, make american great again. Democrats is taking off. We love democrats."
    print("EXAMPLE TWEET:", twt)

    model_len = 20 # ???
    x, x_s = main_clean(twt, model_len)

    prediction = model.predict([x, x_s])
    pro_pol = prediction[:,0]
    print("PRO-TRUMP SCORE:", pro_pol)
    return prediction


if __name__ == "__main__":

    result = test_classify()
    #> ValueError: Layer #2 (named "embedding_1"),
    # weight <tf.Variable 'embedding_1/embeddings:0' shape=(418348, 128) dtype=float32, numpy=array([...]], dtype=float32)>
    # has shape (418348, 128), but the saved weight has shape (418348, 64).

	#model = load_model()
    #while True:
    #    user_text = input("Your Text (press ENTER at any time to quit): ")
    #    if user_text in ["", "exit", "exit()"]: break
    #    results = classify(user_text, model)
    #    print(results)
