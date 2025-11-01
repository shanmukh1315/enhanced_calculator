"""
repl.py
Interactive command-line interface (REPL) for the Enhanced Calculator.
Supports color-coded terminal output for better user experience.
"""

from colorama import Fore, Style, init
from .calculator import Calculator
from .logger import logger

# Initialize colorama (for colored terminal output)
init(autoreset=True)

# List of supported commands
COMMANDS = [
    "add", "subtract", "multiply", "divide",
    "power", "root", "modulus", "int_divide",
    "percent", "abs_diff",
    "history", "clear", "undo", "redo",
    "save", "load", "help", "exit"
]


def print_help():
    """Display available commands and usage examples."""
    print(Fore.CYAN + "\nAvailable commands:")
    for cmd in COMMANDS:
        print(Fore.YELLOW + f"  - {cmd}")

    print(Fore.CYAN + "\nExamples:")
    print(Fore.GREEN + "  add 10 5        → Performs 10 + 5")
    print(Fore.GREEN + "  divide 10 2     → Performs 10 ÷ 2")
    print(Fore.GREEN + "  undo            → Undo last calculation")
    print(Fore.GREEN + "  history         → Show past results")
    print(Fore.GREEN + "  exit            → Quit the program\n")


def main():
    """Main REPL loop."""
    calc = Calculator()
    print(Fore.MAGENTA + Style.BRIGHT + "\n✨ Welcome to the Enhanced Calculator CLI ✨")
    print(Fore.CYAN + "Type 'help' to see all available commands or 'exit' to quit.\n")

    while True:
        try:
            raw = input(Fore.WHITE + Style.BRIGHT + "calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print(Fore.MAGENTA + "\n Goodbye! Thanks for using the Enhanced Calculator.")
            break

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()

        # Exit command
        if cmd == "exit":
            print(Fore.MAGENTA + " Exiting Enhanced Calculator. Goodbye!")
            break

        elif cmd == "help":
            print_help()
            continue

        elif cmd == "history":
            history = calc.history.list()
            if not history:
                print(Fore.RED + "  No calculations yet.")
            else:
                print(Fore.CYAN + "\nCalculation History:")
                for c in history:
                    print(
                        Fore.YELLOW
                        + f"  {c.timestamp} | {c.operation}({c.a}, {c.b}) = {c.result}"
                    )
            continue

        elif cmd == "clear":
            calc.history.clear()
            print(Fore.GREEN + "🧹 History cleared successfully.")
            continue

        elif cmd == "undo":
            undone = calc.history.undo()
            if undone:
                print(
                    Fore.CYAN
                    + f"↩  Undone: {undone.operation}({undone.a}, {undone.b}) = {undone.result}"
                )
            else:
                print(Fore.RED + " Nothing to undo.")
            continue

        elif cmd == "redo":
            redone = calc.history.redo()
            if redone:
                print(
                    Fore.CYAN
                    + f"🔁 Redone: {redone.operation}({redone.a}, {redone.b}) = {redone.result}"
                )
            else:
                print(Fore.RED + "Nothing to redo.")
            continue

        elif cmd == "save":
            calc.save_history()
            print(Fore.GREEN + "History manually saved to file.")
            continue

        elif cmd == "load":
            calc.load_history()
            print(Fore.GREEN + "History loaded from file.")
            continue

        elif cmd in COMMANDS:
            if len(parts) != 3:
                print(Fore.RED + "Usage: command a b  (e.g., add 5 3)")
                continue
            try:
                a, b = parts[1], parts[2]
                result = calc.calculate(cmd, a, b)
                print(Fore.GREEN + f"Result: {result.result}")
            except Exception as e:
                logger.error(f"Error: {e}")
                print(Fore.RED + f" Error: {e}")
            continue

        else:
            print(Fore.RED + f"❓ Unknown command: '{cmd}'. Type 'help' for the list of commands.")


if __name__ == "__main__":
    main()
