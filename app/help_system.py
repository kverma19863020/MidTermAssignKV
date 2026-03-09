class HelpSystem:
    """
    Provides help menu for calculator commands
    """

    def get_help(self):
        return """
Available Commands:

add a b        -> addition
subtract a b   -> subtraction
multiply a b   -> multiplication
divide a b     -> division
power a b      -> a^b
root a b       -> bth root
modulus a b    -> remainder
int_divide a b -> integer division
percent a b    -> (a/b)*100
abs_diff a b   -> absolute difference

history  -> show history
clear    -> clear history
undo     -> undo last calculation
redo     -> redo last calculation
save     -> save history
load     -> load history
help     -> show help
exit     -> exit calculator
"""

def show_help():
    """Function used by calculator.py"""
    help_system = HelpSystem()
    return help_system.get_help()