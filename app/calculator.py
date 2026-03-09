from .operations import OperationFactory
from .calculation import Calculation
from .history import History
from .input_validators import validate_number
from .logger import logger


class Calculator:

    def __init__(self):
        # initialize history
        self.history = History()

    def calculate(self, operation, a, b):

        # validate inputs
        a = validate_number(a)
        b = validate_number(b)

        # get operation
        op = OperationFactory.get_operation(operation)

        # execute operation
        result = op.execute(a, b)

        # create calculation object
        calc = Calculation(operation, a, b, result)

        # store in history
        self.history.add(calc)

        # logging
        logger.info(f"{operation} {a} {b} = {result}")

        return result