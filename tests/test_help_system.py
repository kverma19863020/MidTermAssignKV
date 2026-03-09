from app.help_system import show_help, HelpSystem


def test_show_help_function():

    text = show_help()

    assert "add" in text


def test_help_class():

    help_obj = HelpSystem()

    text = help_obj.get_help()

    assert "exit" in text