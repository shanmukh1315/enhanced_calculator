#  Enhanced Calculator – Command-Line Application
```
An advanced, modular, and fully-tested **Python calculator** featuring multiple arithmetic operations, undo/redo with the **Memento Pattern**, live logging and auto-saving via the **Observer Pattern**, and factory-based operation management.  
This project also integrates **CI/CD automation with GitHub Actions** and achieves **100% unit test coverage**.

```

## Badges
```
![Python application](https://github.com/shanmukh1315/enhanced_calculator/actions/workflows/python-app.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
```

## Features
```
### Core Functionalities
- **Arithmetic Operations**
  - Addition, Subtraction, Multiplication, Division  
  - Power, Root, Modulus, Integer Division  
  - Percentage Calculation, Absolute Difference
- **Undo/Redo** history using **Memento Pattern**
- **Logging and Auto-Save** via **Observer Pattern**
- **Dynamic History Management** (save/load using CSV and `pandas`)
- **Environment-Driven Configuration** via `.env`
- **Color-Coded CLI Interface** (powered by `colorama`)
```

## Design Patterns Implemented
```
| Pattern | Purpose |
|----------|----------|
| **Factory** | Creates operation instances dynamically |
| **Observer** | Automatically logs and saves calculations |
| **Memento** | Enables undo/redo functionality |
| **REPL (Interactive Loop)** | Provides an interactive command-line experience |
```


## Project Structure
```
enhanced-calculator/
├── app/
│ ├── init.py
│ ├── calculator.py
│ ├── calculation.py
│ ├── calculator_config.py
│ ├── calculator_memento.py
│ ├── exceptions.py
│ ├── history.py
│ ├── input_validators.py
│ ├── operations.py
│ ├── logger.py
│ └── repl.py
├── tests/
│ ├── init.py
│ ├── test_calculator.py
│ ├── test_calculation.py
│ ├── test_history.py
│ ├── test_operations.py
│ └── ...
├── .github/workflows/python-app.yml
├── .env
├── requirements.txt
├── README.md
└── venv/

```


## Configuration (`.env` Example)

```
# Logging
CALCULATOR_LOG_DIR=logs
CALCULATOR_LOG_FILE=calculator.log

# History
CALCULATOR_HISTORY_DIR=history
CALCULATOR_HISTORY_FILE=history.csv
CALCULATOR_MAX_HISTORY_SIZE=50
CALCULATOR_AUTO_SAVE=true

# Limits
CALCULATOR_PRECISION=4
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8


nstallation & Setup
# Clone repository
git clone https://github.com/shanmukh1315/enhanced_calculator.git
cd enhanced_calculator

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # on macOS/Linux
venv\Scripts\activate     # on Windows

# Install dependencies
pip install -r requirements.txt

Usage (REPL CLI)

Run the interactive calculator:

python -m app.repl
```

**Supported Commands**
```
Command	                   Description
add 10 5	               Adds two numbers
subtract 20 10	         Subtracts one number from another
multiply 3 7	           Multiplies numbers
divide 20 4	             Divides numbers
power 2 3	               Exponentiation
root 27 3	               Cube root
modulus 10 3	           Remainder of division
int_divide 10 3	         Integer division
percent 10 100	         Calculate percentage
abs_diff 10 3	           Absolute difference
undo, redo	             Undo/redo last action
history, clear	         View or clear history
save, load	             Save/load calculation history
help	                   Show all commands
exit	                   Exit the calculator
```
**Example Output**
```
calc> add 10 5
 Result: 15.0

calc> power 2 3
 Result: 8.0

calc> undo
Undone: power(2.0, 3.0) = 8.0

calc> redo
Redone: power(2.0, 3.0) = 8.0
```
** Testing & Coverage**
```
Run all tests with coverage:

pytest --cov=app --cov-fail-under=100

```
Expected output:
```
venv) (base) shannu@Shannus-MacBook-Air enhanced-calculator % venv/bin/pytest --cov=app --cov-fail-under=100

=========================================== test session starts ============================================
platform darwin -- Python 3.12.4, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/shannu/Desktop/MS/web_API/enhanced-calculator
configfile: .pytest.ini
plugins: cov-7.0.0
collected 21 items                                                                                         

tests/test_calculation.py .                                                                          [  4%]
tests/test_calculator.py .....                                                                       [ 28%]
tests/test_extra_operations.py ...                                                                   [ 42%]
tests/test_history.py ....                                                                           [ 61%]
tests/test_input_validators.py ...                                                                   [ 76%]
tests/test_operations.py .....                                                                       [100%]

============================================== tests coverage ==============================================
_____________________________ coverage: platform darwin, python 3.12.4-final-0 _____________________________

Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
app/calculation.py              9      0   100%
app/calculator.py              56      0   100%
app/calculator_config.py       14      0   100%
app/calculator_memento.py       6      0   100%
app/exceptions.py               6      0   100%
app/history.py                 26      0   100%
app/input_validators.py        12      0   100%
app/logger.py                   6      0   100%
app/operations.py              50      0   100%
---------------------------------------------------------
TOTAL                         185      0   100%
Required test coverage of 100% reached. Total coverage: 100.00%
============================================ 21 passed in 0.52s ============================================
```



