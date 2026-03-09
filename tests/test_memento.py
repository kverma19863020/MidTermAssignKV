from app.calculator_memento import Caretaker


def test_save_state():
    caretaker = Caretaker()

    caretaker.save("state1")

    assert len(caretaker.undo_stack) == 1


def test_multiple_saves():
    caretaker = Caretaker()

    caretaker.save("state1")
    caretaker.save("state2")

    assert len(caretaker.undo_stack) == 2


def test_undo_last_state():
    caretaker = Caretaker()

    caretaker.save("state1")
    caretaker.save("state2")

    state = caretaker.undo()

    assert state == "state2"


def test_undo_empty():
    caretaker = Caretaker()

    result = caretaker.undo()

    assert result is None