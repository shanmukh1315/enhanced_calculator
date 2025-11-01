import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory of the project (one level above /app)
BASE_DIR = Path(__file__).resolve().parent.parent

# Load variables from .env
load_dotenv()

def _ensure_dir(path: str):
    """Create a directory if it doesn't exist and return the path."""
    p = BASE_DIR / path
    p.mkdir(parents=True, exist_ok=True)
    return p

# --- Load environment variables with defaults ---
LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "history")

# Make sure directories exist
_ensure_dir(LOG_DIR)
_ensure_dir(HISTORY_DIR)

CONFIG = {
    "LOG_DIR": LOG_DIR,
    "HISTORY_DIR": HISTORY_DIR,
    "MAX_HISTORY_SIZE": int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100")),
    "AUTO_SAVE": os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true",
    "PRECISION": int(os.getenv("CALCULATOR_PRECISION", "4")),
    "MAX_INPUT_VALUE": float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000")),
    "DEFAULT_ENCODING": os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8"),
    "HISTORY_FILE": os.getenv("CALCULATOR_HISTORY_FILE", f"{HISTORY_DIR}/calculation_history.csv"),
    "LOG_FILE": os.getenv("CALCULATOR_LOG_FILE", f"{LOG_DIR}/calculator.log"),
}
