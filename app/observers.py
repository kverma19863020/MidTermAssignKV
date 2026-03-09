"""
Observer Pattern implementation.
"""

class Observer:
    """Base observer class."""

    def update(self, message: str):
        pass


class LoggingObserver(Observer):
    """Observer that logs calculator messages."""

    def update(self, message: str):
        print(message)