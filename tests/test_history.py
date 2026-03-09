from app.history import History
from app.calculation import Calculation


def test_history_initial():
    history = History()
    assert history.records == []


def test_add_history():
    history = History()

    calc = Calculation("add", 1, 2, 3)
    history.add(calc)

    assert len(history.records) == 1


def test_multiple_history():
    history = History()

    history.add(Calculation("add", 1, 2, 3))
    history.add(Calculation("subtract", 5, 3, 2))
    history.add(Calculation("multiply", 2, 4, 8))

    assert len(history.records) == 3


def test_to_dataframe():
    history = History()

    history.add(Calculation("add", 1, 2, 3))
    history.add(Calculation("multiply", 2, 3, 6))

    df = history.to_dataframe()

    assert len(df) == 2
    assert "operation" in df.columns


def test_empty_dataframe():
    history = History()

    df = history.to_dataframe()

    assert df.empty


def test_clear_history():
    history = History()

    history.add(Calculation("add", 1, 2, 3))
    history.clear()

    assert len(history.records) == 0