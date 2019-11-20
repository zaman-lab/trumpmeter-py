
from keras.models import Model

from app.helper_text import main_clean

class SuperModel(Model):
	""" Adds a custom high-level classification method to the keras model """

	def classify(self, txt):
		"""txt (str) the text to classify"""
		x, x_s = main_clean(txt)

		results = self.predict([x, x_s])
		results = results[0]
		pro_score = round(float(results[1]), 4)
		response = {"text": txt, "pro_trump": pro_score}
		return response
