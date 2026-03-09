from abc import ABC, abstractmethod
from .exceptions import DivisionByZeroError


class Operation(ABC):

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass


class Addition(Operation):

    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtraction(Operation):

    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiplication(Operation):

    def execute(self, a: float, b: float) -> float:
        return a * b


class Division(Operation):

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero.")
        return a / b


class OperationFactory:

    operations = {
        "add": Addition(),
        "subtract": Subtraction(),
        "multiply": Multiplication(),
        "divide": Division(),
    }

    @staticmethod
    def get_operation(name: str):
        if name not in OperationFactory.operations:
            raise ValueError(f"Invalid operation '{name}'")

        return OperationFactory.operations[name]