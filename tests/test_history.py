from app.history import HistoryManager
from app.calculation import Calculation


def test_history_save():

    history = HistoryManager()

    calc = Calculation(2, 3, "add", 5)

    history.save(calc)

    data = history.get_all()

    assert len(data) >= 1