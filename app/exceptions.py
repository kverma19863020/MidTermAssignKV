class CalculatorError(Exception):
    """Base exception for calculator"""
    pass


class OperationError(CalculatorError):
    """Raised when an invalid operation occurs"""
    pass


class ValidationError(CalculatorError):
    """Raised when input validation fails"""
    pass


class DivisionByZeroError(OperationError):
    """Raised when division by zero occurs"""
    pass