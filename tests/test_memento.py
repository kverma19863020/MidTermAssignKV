from app.calculator_memento import Caretaker


def test_undo_empty():

    caretaker = Caretaker()

    assert caretaker.undo() is None