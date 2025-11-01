import logging
from pathlib import Path
from .calculator_config import CONFIG, BASE_DIR

# Path to the log file (from .env)
LOG_FILE = BASE_DIR / CONFIG["LOG_FILE"]

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),   # Log to file
        logging.StreamHandler()          # Also show logs in console
    ]
)

# Create a named logger instance
logger = logging.getLogger("calculator")
