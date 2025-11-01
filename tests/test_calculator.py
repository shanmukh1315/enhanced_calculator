import os
import pandas as pd
from pathlib import Path
from app.calculator import Calculator
from app.calculation import Calculation
from app.calculator_config import CONFIG


def test_calculator_add():
    calc = Calculator()
    result = calc.calculate("add", 10, 5)
    assert result.result == 15


def test_calculator_power():
    calc = Calculator()
    result = calc.calculate("power", 2, 3)
    assert result.result == 8


def test_calculator_history_adds():
    calc = Calculator()
    calc.calculate("add", 1, 1)
    calc.calculate("multiply", 2, 3)
    assert len(calc.history.list()) >= 2


def test_calculator_save_and_load(tmp_path):
    """Test manual save and load from a temporary CSV."""
    calc = Calculator()
    calc.calculate("add", 2, 3)
    calc.calculate("subtract", 10, 4)

    # ✅ FIX: use full absolute path, not just filename
    temp_file = tmp_path / "test_history.csv"
    CONFIG["HISTORY_FILE"] = str(temp_file.resolve())

    calc.save_history()
    assert temp_file.exists(), f"Expected file {temp_file} to exist"

    # Clear and reload
    calc.history.clear()
    calc.load_history()
    assert len(calc.history.list()) == 2


def test_load_history_file_not_found(tmp_path):
    """Ensure loading non-existent history file starts fresh."""
    calc = Calculator()

    # ✅ FIX: use a guaranteed non-existent absolute file path
    temp_file = tmp_path / "nonexistent.csv"
    CONFIG["HISTORY_FILE"] = str(temp_file.resolve())

    # Ensure old in-memory history is cleared
    calc.history.clear()

    # Run method
    calc.load_history()

    # Confirm no data in memory after failed load
    assert len(calc.history.list()) == 0
