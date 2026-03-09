import os
from app.history import History
from app.calculation import Calculation


def test_history_add():

    history = History()

    calc = Calculation("add", 1, 2, 3)

    history.add(calc)

    assert len(history.records) == 1


def test_history_clear():

    history = History()

    calc = Calculation("add", 1, 2, 3)

    history.add(calc)

    history.clear()

    assert len(history.records) == 0


def test_history_save_and_load():

    history = History()

    calc = Calculation("add", 1, 2, 3)

    history.add(calc)

    history.save()

    new_history = History()

    new_history.load()

    assert len(new_history.records) >= 0