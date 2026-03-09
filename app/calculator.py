"""
Main calculator controller.

Coordinates:
- operations
- history
- undo system
- validation
- logging
"""

from .operations import OperationFactory
from .calculation import Calculation
from .history import HistoryManager
from .calculator_memento import CalculatorMemento, Caretaker
from .input_validators import validate_number
from .observers import LoggingObserver
from .help_system import show_help


class Calculator:
    """
    Main calculator class.
    """

    def __init__(self):

        # History manager handles CSV storage
        self.history_manager = HistoryManager()

        # Caretaker manages undo states
        self.caretaker = Caretaker()

        # Observer logs operations
        self.observer = LoggingObserver()

    def calculate(self, operation_name: str, a: float, b: float):
        """
        Perform calculation using factory pattern.
        """

        operation = OperationFactory.get_operation(operation_name)

        result = operation.execute(a, b)

        # Create calculation record
        calculation = Calculation(a, b, operation_name, result)

        # Save to CSV history
        self.history_manager.save(calculation)

        # Save state for undo functionality
        self.caretaker.save(CalculatorMemento(calculation))

        # Notify observer
        self.observer.update(
            f"Performed {operation_name} on {a} and {b} = {result}"
        )

        return result

    def undo(self):
        """
        Undo last calculation.
        """

        memento = self.caretaker.undo()

        if memento:
            print("Last calculation undone.")

        else:
            print("Nothing to undo.")

    def show_history(self):
        """
        Display calculation history.
        """

        history = self.history_manager.get_all()

        for record in history:
            print(record)

    def run(self):
        """
        REPL loop (command-line interface).
        """

        show_help()

        while True:

            command = input("Enter command: ").strip().lower()

            if command == "exit":
                break

            elif command == "help":
                show_help()

            elif command == "history":
                self.show_history()

            elif command == "undo":
                self.undo()

            else:
                try:

                    # Collect user input
                    a = validate_number(input("Enter first number: "))
                    b = validate_number(input("Enter second number: "))

                    result = self.calculate(command, a, b)

                    print("Result:", result)

                except Exception as e:
                    print("Error:", e)


# Entry point for program execution
if __name__ == "__main__":
    calc = Calculator()
    calc.run()