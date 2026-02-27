import csv
import os
from .calculation import Calculation


class HistoryManager:
    FILE_PATH = "history/history.csv"

    def __init__(self):
        os.makedirs("history", exist_ok=True)

    def save(self, calculation: Calculation):
        file_exists = os.path.isfile(self.FILE_PATH)

        with open(self.FILE_PATH, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(
                    ["operand1", "operand2", "operation", "result", "timestamp"]
                )
            writer.writerow(
                [
                    calculation.operand1,
                    calculation.operand2,
                    calculation.operation,
                    calculation.result,
                    calculation.timestamp,
                ]
            )

    def get_all(self):
        if not os.path.exists(self.FILE_PATH):
            return []

        with open(self.FILE_PATH, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)