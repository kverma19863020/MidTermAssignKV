from app.operations import Addition, Subtraction, Multiplication, Division


def test_add():
    assert Addition().execute(2, 3) == 5


def test_subtract():
    assert Subtraction().execute(5, 3) == 2


def test_multiply():
    assert Multiplication().execute(4, 2) == 8


def test_divide():
    assert Division().execute(10, 2) == 5