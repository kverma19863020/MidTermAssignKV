"""
Implements the Observer Design Pattern.

Observers react to events such as completed calculations.
"""

from .logger import logger


class Observer:
    """
    Base observer interface.
    """

    def update(self, message: str):
        pass


class LoggingObserver(Observer):
    """
    Logs events whenever a calculation occurs.
    """

    def update(self, message: str):

        # Send message to logging system
        logger.info(message)