class CalculatorException(Exception):
    """Base exception for calculator errors."""
    pass

class DivisionByZeroError(CalculatorException):
    """Raised when attempting division by zero."""
    pass


class InvalidOperationError(CalculatorException):
    """Raised when an invalid operation is requested."""
    pass


class InvalidInputError(CalculatorException):
    """Raised when invalid input is provided."""
    pass