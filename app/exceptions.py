"""
Custom exception classes for the calculator application.
These provide clearer error handling across the project.
"""

class CalculatorException(Exception):
    """Base exception for calculator-related errors."""
    pass

class DivisionByZeroError(CalculatorException):
    """Raised when attempting to divide a number by zero."""
    pass

class InvalidOperationError(CalculatorException):
    """Raised when an unsupported operation is requested."""
    pass

class InvalidInputError(CalculatorException):
    """Raised when user input cannot be converted to a number."""
    pass