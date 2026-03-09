from app.calculator_memento import Caretaker


def test_memento_save_and_undo():

    caretaker = Caretaker()

    caretaker.save("state1")
    caretaker.save("state2")

    state = caretaker.undo()

    assert state == "state2"


def test_memento_redo():

    caretaker = Caretaker()

    caretaker.save("state1")
    caretaker.save("state2")

    caretaker.undo()

    state = caretaker.redo()

    assert state == "state2"