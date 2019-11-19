

from app.model import saved_model, weighted_model
from app.client import classify

def test_original_classifications():

    model = weighted_model()

    r1 = classify("Make america great again! Trump for President! #MAGA", model)
    #assert round(float(r1["pro_trump"]), 4) == 0.6885
    assert r1["temp"] == [0.3115, 0.6885]

    r2 = classify("RT @someuser: Trump is, by far, the best POTUS in history. \n\nBonus: He^s friggin^ awesome!\n\nTrump gave Pelosi and the Dems the ultimate\u2026 ", model)
    #assert round(float(r2["pro_trump"]), 4) == 0.2985
    assert r2["temp"] == [0.7015, 0.2985]

    r3 = classify("If Trump wins I'm moving to Canada #StrongerTogether", model)
    #assert round(float(r3["pro_trump"]), 4) == 0.0616
    assert r3["temp"] == [0.9384, 0.0616]

    r4 = classify("RT @MotherJones: A scientist who resisted Trump administration censorship of climate report just lost her job", model)
    #assert round(float(r4["pro_trump"]), 4) == 0.0018
    assert r4["temp"] == [0.9982, 0.0018]

def test_final_classifications():

    model = saved_model()

    r1 = classify("Make america great again! Trump for President! #MAGA", model)
    #assert round(float(r1["pro_trump"]), 4) == 0.9867
    assert r1["temp"] == [0.0133, 0.9867]

    r2 = classify("RT @someuser: Trump is, by far, the best POTUS in history. \n\nBonus: He^s friggin^ awesome!\n\nTrump gave Pelosi and the Dems the ultimate\u2026 ", model)
    #assert round(float(r2["pro_trump"]), 4) == 0.9928
    assert r2["temp"] == [0.0072, 0.9928]

    r3 = classify("If Trump wins I'm moving to Canada #StrongerTogether", model)
    #assert round(float(r3["pro_trump"]), 4) == 0.0
    assert r3["temp"] == [1.0, 0.0]

    r4 = classify("RT @MotherJones: A scientist who resisted Trump administration censorship of climate report just lost her job", model)
    #assert round(float(r4["pro_trump"]), 4) == 0.0
    assert r4["temp"] == [1.0, 0.0]
