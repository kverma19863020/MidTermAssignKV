import pytest
from app.operations import Addition, Subtraction, Multiplication, Division, OperationFactory
from app.exceptions import DivisionByZeroError


def test_addition():
    op = Addition()
    assert op.execute(2, 3) == 5


def test_subtraction():
    op = Subtraction()
    assert op.execute(5, 3) == 2


def test_multiplication():
    op = Multiplication()
    assert op.execute(4, 3) == 12


def test_division():
    op = Division()
    assert op.execute(10, 2) == 5


def test_division_by_zero():
    op = Division()

    with pytest.raises(DivisionByZeroError):
        op.execute(10, 0)


def test_operation_factory_add():
    op = OperationFactory.get_operation("add")

    assert op.execute(1, 2) == 3


def test_invalid_operation():
    with pytest.raises(ValueError):
        OperationFactory.get_operation("invalid")