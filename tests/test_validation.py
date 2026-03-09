import pytest
from app.input_validators import validate_number
from app.exceptions import ValidationError


def test_validate_integer():
    assert validate_number("5") == 5.0


def test_validate_float():
    assert validate_number("3.5") == 3.5


def test_validate_negative():
    assert validate_number("-2") == -2.0


def test_validate_invalid():
    with pytest.raises(ValidationError):
        validate_number("abc")