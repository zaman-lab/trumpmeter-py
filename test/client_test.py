

from app.model import original_model, saved_final_model, reconstructed_final_model
from app.client import classify

def test_original_classifications():

    model = original_model()

    r1 = classify("Make america great again! Trump for President! #MAGA", model)
    #assert r1["pro_trump"] == [0.3115, 0.6885]
    assert round(float(r1["pro_trump"]), 4) == 0.6885

    r2 = classify("RT @someuser: Trump is, by far, the best POTUS in history. \n\nBonus: He^s friggin^ awesome!\n\nTrump gave Pelosi and the Dems the ultimate\u2026 ", model)
    #assert r2["pro_trump"] == [0.7015, 0.2985]
    assert round(float(r2["pro_trump"]), 4) == 0.2985

    r3 = classify("If Trump wins I'm moving to Canada #StrongerTogether", model)
    #assert r3["pro_trump"] == [0.9384, 0.0616]
    assert round(float(r3["pro_trump"]), 4) == 0.0616

    r4 = classify("RT @MotherJones: A scientist who resisted Trump administration censorship of climate report just lost her job", model)
    #assert r4["pro_trump"] == [0.9982, 0.0018]
    assert round(float(r4["pro_trump"]), 4) == 0.0018

def test_final_classifications():

    # these two models should give the same results
    model_from_file = saved_final_model()
    model_from_weights = reconstructed_final_model()

    for model in [model_from_file, model_from_weights]:

        r1 = classify("Make america great again! Trump for President! #MAGA", model)
        #assert r1["pro_trump"] == [0.0133, 0.9867]
        assert round(float(r1["pro_trump"]), 4) == 0.9867

        r2 = classify("RT @someuser: Trump is, by far, the best POTUS in history. \n\nBonus: He^s friggin^ awesome!\n\nTrump gave Pelosi and the Dems the ultimate\u2026 ", model)
        #assert r2["pro_trump"] == [0.0072, 0.9928]
        assert round(float(r2["pro_trump"]), 4) == 0.9928

        r3 = classify("If Trump wins I'm moving to Canada #StrongerTogether", model)
        #assert r3["pro_trump"] == [1.0, 0.0]
        assert round(float(r3["pro_trump"]), 4) == 0.0

        r4 = classify("RT @MotherJones: A scientist who resisted Trump administration censorship of climate report just lost her job", model)
        #assert r4["pro_trump"] == [1.0, 0.0]
        assert round(float(r4["pro_trump"]), 4) == 0.0
