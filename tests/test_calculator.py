from app.calculator import Calculator


def test_history_recorded():

    calc = Calculator()

    calc.calculate("add", 1, 2)

    assert len(calc.history.records) == 1

def test_multiple_calculations():

    calc = Calculator()

    calc.calculate("add", 1, 2)
    calc.calculate("multiply", 2, 3)

    assert len(calc.history.records) == 2