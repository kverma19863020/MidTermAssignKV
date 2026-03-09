import pandas as pd


class History:
    """
    Stores all calculator calculations.
    Provides methods to add, clear, and convert history to DataFrame.
    """

    def __init__(self):
        self.records = []

    def add(self, calculation):
        """Add a calculation object to history."""
        self.records.append(calculation)

    def clear(self):
        """Clear all history."""
        self.records = []

    def to_dataframe(self):
        """Convert history to pandas DataFrame."""

        if not self.records:
            return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

        data = []

        for calc in self.records:
            data.append(
                {
                    "operation": calc.operation,
                    "operand1": calc.a,
                    "operand2": calc.b,
                    "result": calc.result,
                }
            )

        return pd.DataFrame(data)