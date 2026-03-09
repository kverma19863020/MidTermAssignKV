class CalculatorMemento:
    """
    Memento class that stores calculator state
    """

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    """
    Caretaker manages undo and redo stacks
    """

    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save(self, state):
        """Save state for undo"""
        self.undo_stack.append(CalculatorMemento(state))
        self.redo_stack.clear()

    def undo(self):
        """Undo last state"""
        if not self.undo_stack:
            return None

        memento = self.undo_stack.pop()
        self.redo_stack.append(memento)
        return memento.get_state()

    def redo(self):
        """Redo previously undone state"""
        if not self.redo_stack:
            return None

        memento = self.redo_stack.pop()
        self.undo_stack.append(memento)
        return memento.get_state()