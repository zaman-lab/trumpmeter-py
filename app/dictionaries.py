
import os
from gensim.corpora import Dictionary

DICTIONARIES_DIRPATH = os.path.join(os.path.dirname(__file__), "..", "Dictionary")

def load_dictionaries():
	print("LOADING DICTIONARIES...")
	dict1 = Dictionary.load(os.path.join(DICTIONARIES_DIRPATH, "dic.txt"))
	dict2 = Dictionary.load(os.path.join(DICTIONARIES_DIRPATH, "dic_s.txt"))
	return dict1, dict2

if __name__ == "__main__":

	texts = [
		['human', 'interface', 'computer']
	]
	my_dict = Dictionary(texts)
	for s in my_dict.iteritems():
		print(s)

	d1, d2 = load_dictionaries()

	print("-----------------------------")
	print("DICTIONARY 1", type(d1), len(d1))
	for s in d1.iteritems():
		print(s)

	print("-----------------------------")
	print("DICTIONARY 2", type(d2), len(d2))
	for s in d2.iteritems():
		print(s)
