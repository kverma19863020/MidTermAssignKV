class Memento:
    """
    Stores a snapshot of calculator state.
    """

    def __init__(self, state):
        self.state = state


class Caretaker:
    """
    Manages saved states for undo functionality.
    """

    def __init__(self):
        self.undo_stack = []

    def save(self, state):
        """Save a new state."""
        self.undo_stack.append(Memento(state))

    def undo(self):
        """Restore last state."""

        if not self.undo_stack:
            return None

        memento = self.undo_stack.pop()
        return memento.state