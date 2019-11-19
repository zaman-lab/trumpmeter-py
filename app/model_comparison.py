
from pprint import pprint
import os

from conftest import EXAMPLE_TWEETS
from app.client import classify
from app.model import original_model, saved_final_model, reconstructed_final_model
from app.helper_text import main_clean

if __name__ == "__main__":

    model_o = original_model()
    model_f = saved_final_model()
    model_r = reconstructed_final_model()

    for twt in EXAMPLE_TWEETS:
        print("\n-----------------------------")
        print(f"TWEET: '{twt}'")
        response_o = classify(twt, model_o)
        print("ORIG:", response_o["pro_trump"])
        response_f = classify(twt, model_f)
        print("FINAL:", response_f["pro_trump"])
        response_r = classify(twt, model_r)
        print("RECONST:", response_r["pro_trump"])

    exit()

    model = model_r
    while True:
        user_text = input("Your Text (press ENTER at any time to quit): ")
        if user_text in ["", "exit", "exit()"]: break
        results = classify(user_text, model)
        pprint(results)
        print("-----------------------------")
