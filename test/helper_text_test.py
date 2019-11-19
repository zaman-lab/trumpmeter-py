
import string

from app.helper_text import main_clean, clean

def test_clean():
    # it removes stopwords and punctuation, and lowercases the results:
    assert clean("Hello world! is a message from me and us") == "hello world message us"

def test_main_clean():
    # it converts text into a vector:
    results = main_clean("Hello world")
    assert results[0].tolist() == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8363, 1774]]
    assert results[1].tolist() == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8320, 1782]]

def test_remove_punctuation():
    cleaned = "Hello world!".translate(str.maketrans('', '', string.punctuation))
    assert "!" not in cleaned
