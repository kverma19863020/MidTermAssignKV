from .exceptions import ValidationError


def validate_number(value):
    """
    Validate input and convert to float.
    """

    try:
        number = float(value)
    except ValueError:
        raise ValidationError("Input must be a number")

    return number