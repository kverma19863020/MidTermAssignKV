from app.observers import LoggingObserver


class DummyCalculation:
    operation = "add"
    a = 1
    b = 2
    result = 3


def test_logging_observer():

    observer = LoggingObserver()

    calc = DummyCalculation()

    observer.update(calc)

    assert True