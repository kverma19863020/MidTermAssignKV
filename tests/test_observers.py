from app.observers import Observer, LoggingObserver


def test_observer_update():
    observer = Observer()

    observer.update("test")

    assert observer is not None


def test_logging_observer_update():
    observer = LoggingObserver()

    observer.update("calculator used")

    assert observer is not None