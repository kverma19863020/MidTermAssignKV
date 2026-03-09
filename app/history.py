import pandas as pd
import os
from .calculator_config import CalculatorConfig


class History:
    """Stores calculator history"""

    def __init__(self):
        self.records = []

    def add(self, calculation):
        self.records.append(calculation)

    def clear(self):
        self.records = []

    def to_dataframe(self):
        return pd.DataFrame([c.to_dict() for c in self.records])

    def save(self):

        os.makedirs(CalculatorConfig.HISTORY_DIR, exist_ok=True)

        file_path = f"{CalculatorConfig.HISTORY_DIR}/history.csv"

        df = self.to_dataframe()

        df.to_csv(file_path, index=False)

    def load(self):

        file_path = f"{CalculatorConfig.HISTORY_DIR}/history.csv"

        if not os.path.exists(file_path):
            return

        df = pd.read_csv(file_path)

        self.records = df.to_dict("records")