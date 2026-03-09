"""
Operation classes implementing the Factory Pattern.
Each mathematical operation inherits from the abstract
Operation base class and implements the execute method.
"""
from abc import ABC, abstractmethod
from .exceptions import DivisionByZeroError

class Operation(ABC):
    """
    Abstract base class defining the structure for operations.
    Every operation must implement the execute method.
    """

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass


class Addition(Operation):
    """Handles addition operation."""

    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtraction(Operation):
    """Handles subtraction operation."""

    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiplication(Operation):
    """Handles multiplication operation."""

    def execute(self, a: float, b: float) -> float:
        return a * b


class Division(Operation):
    """Handles division operation."""

    def execute(self, a: float, b: float) -> float:

        # Prevent division by zero
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero.")

        return a / b

class OperationFactory:
    """
    Factory Pattern implementation.

    This class centralizes creation of operation objects.
    It prevents calculator logic from needing to know
    how operations are constructed.
    """
    operations = {
        "add": Addition(),
        "subtract": Subtraction(),
        "multiply": Multiplication(),
        "divide": Division(),
    }
    @staticmethod
    def get_operation(name: str) -> Operation:
        """
        Retrieve an operation object by name.
        """

        if name not in OperationFactory.operations:
            raise ValueError(f"Invalid operation '{name}'")

        return OperationFactory.operations[name]