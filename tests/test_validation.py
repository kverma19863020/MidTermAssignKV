from app.input_validators import validate_number


def test_float_input():

    assert validate_number("10.5") == 10.5