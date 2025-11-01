from app.history import HistoryManager
from app.calculation import Calculation


def test_undo_and_redo():
    """Test undo/redo functionality after adding calculations."""
    h = HistoryManager()
    c1 = Calculation("add", 2, 3, 5)
    c2 = Calculation("subtract", 5, 2, 3)

    h.add(c1)
    h.add(c2)
    assert len(h.list()) == 2

    # Undo last operation
    undone = h.undo()
    assert undone.result == 3
    assert len(h.list()) == 1

    # Redo it back
    redone = h.redo()
    assert redone.result == 3
    assert len(h.list()) == 2


def test_clear_history():
    """Test that clearing the history works correctly."""
    h = HistoryManager()
    c = Calculation("add", 1, 1, 2)
    h.add(c)
    h.clear()
    assert len(h.list()) == 0


def test_undo_redo_empty():
    """Test undo/redo return None when stacks are empty."""
    h = HistoryManager()
    assert h.undo() is None
    assert h.redo() is None


def test_add_and_list_history():
    """Test that history adds and lists calculations correctly."""
    h = HistoryManager()
    c1 = Calculation("multiply", 3, 4, 12)
    c2 = Calculation("divide", 8, 2, 4)

    h.add(c1)
    h.add(c2)
    results = [c.result for c in h.list()]

    assert results == [12, 4]
    assert len(h.list()) == 2
