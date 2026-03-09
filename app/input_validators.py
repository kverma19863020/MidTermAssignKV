from .exceptions import ValidationError
from .calculator_config import CalculatorConfig

def validate_number(value):

    try:
        number = float(value)
    except ValueError:
        raise ValidationError("Input must be a number")

    if abs(number) > CalculatorConfig.MAX_INPUT:
        raise ValidationError("Input exceeds maximum allowed value")

    return number