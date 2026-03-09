from app.calculation import Calculation


def test_calculation():

    c = Calculation("add", 1, 2, 3)

    assert c.result == 3