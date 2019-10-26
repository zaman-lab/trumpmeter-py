
from gensim.corpora import Dictionary

from app.dictionaries import load_dictionaries

def test_load_dictionaries():

    d1, d2 = load_dictionaries()

    assert isinstance(d1, Dictionary)
    assert isinstance(d2, Dictionary)

    assert len(d1) == 41_8347
    assert len(d2) == 40_4278

    assert "antiracism" in d1.values()
    assert "antiracism" in d2.values()
    assert d1[124813] == "antiracism"
    assert d1.id2token[124813] == "antiracism"
    assert d1.token2id["antiracism"] == 124813

    assert d1.token2id["pizzagate"] == 16052
    assert d2.token2id["pizzagate"] == 63088
