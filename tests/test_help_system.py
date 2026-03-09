from app.help_system import HelpSystem

def test_help_menu():

    help_system = HelpSystem()

    text = help_system.get_help()

    assert "add" in text