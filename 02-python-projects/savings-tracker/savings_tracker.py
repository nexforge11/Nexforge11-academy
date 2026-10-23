# ==========================================
# NEXFORGE11 ACADEMY
# STAGE 2 - PYTHON PROJECTS
# PROJECT: SAVINGS TRACKER (command line)
# ==========================================
#
# Builds on the Lesson 01 mini project (mini_project_savings_tracker.ipynb).
# New ideas used here: functions, lists, dictionaries, loops, input,
# error handling and saving data to a JSON file.
#
# Run it with:  python savings_tracker.py

import json
import os
from datetime import date

DATA_FILE = "savings_data.json"


# ---------- Working with the data ----------

def new_tracker(goal):
    """Create an empty tracker with a savings goal."""
    if goal <= 0:
        raise ValueError("The goal must be more than 0.")
    return {"goal": goal, "transactions": []}


def add_transaction(tracker, amount, note="", when=None):
    """Record money in (positive amount) or money out (negative amount)."""
    if amount == 0:
        raise ValueError("The amount cannot be 0.")
    if amount < 0 and -amount > balance(tracker):
        raise ValueError("You cannot withdraw more than you have saved.")
    tracker["transactions"].append({
        "date": when or date.today().isoformat(),
        "amount": amount,
        "note": note,
    })


def balance(tracker):
    """Add up every transaction to get the current savings."""
    total = 0
    for transaction in tracker["transactions"]:
        total = total + transaction["amount"]
    return total


def remaining(tracker):
    """How much more is needed to reach the goal (never below 0)."""
    return max(tracker["goal"] - balance(tracker), 0)


def progress_percent(tracker):
    """Progress toward the goal as a percentage, capped at 100."""
    percent = balance(tracker) / tracker["goal"] * 100
    return min(round(percent, 1), 100)


def progress_bar(tracker, width=20):
    """Draw progress as text, e.g. [########------------]."""
    filled = int(progress_percent(tracker) / 100 * width)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


# ---------- Saving and loading ----------

def save(tracker, path=DATA_FILE):
    with open(path, "w") as file:
        json.dump(tracker, file, indent=2)


def load(path=DATA_FILE):
    """Return the saved tracker, or None if nothing has been saved yet."""
    if not os.path.exists(path):
        return None
    with open(path) as file:
        return json.load(file)


# ---------- Talking to the user ----------

def ask_amount(prompt):
    """Keep asking until the user types a positive number."""
    while True:
        text = input(prompt)
        try:
            amount = float(text)
        except ValueError:
            print("Please type a number, e.g. 25 or 12.50")
            continue
        if amount <= 0:
            print("Please type a number bigger than 0.")
            continue
        return amount


def show_summary(tracker):
    print()
    print("Goal:     ", format_money(tracker["goal"]))
    print("Saved:    ", format_money(balance(tracker)))
    print("Remaining:", format_money(remaining(tracker)))
    print(progress_bar(tracker), str(progress_percent(tracker)) + "%")
    if remaining(tracker) == 0:
        print("Goal reached - well done!")


def show_history(tracker):
    print()
    if not tracker["transactions"]:
        print("No transactions yet.")
        return
    for transaction in tracker["transactions"]:
        sign = "+" if transaction["amount"] > 0 else "-"
        line = transaction["date"] + "  " + sign + format_money(abs(transaction["amount"]))
        if transaction["note"]:
            line = line + "  " + transaction["note"]
        print(line)


def format_money(amount):
    return f"{amount:,.2f}"


def main():
    print("=== Nexforge11 Savings Tracker ===")
    tracker = load()
    if tracker is None:
        goal = ask_amount("What is your savings goal? ")
        tracker = new_tracker(goal)
        save(tracker)

    while True:
        print()
        print("1. Add a deposit")
        print("2. Make a withdrawal")
        print("3. Show summary")
        print("4. Show history")
        print("5. Change goal")
        print("6. Quit")
        choice = input("Choose 1-6: ").strip()

        try:
            if choice == "1":
                amount = ask_amount("Deposit amount: ")
                note = input("Note (optional): ")
                add_transaction(tracker, amount, note)
                save(tracker)
                show_summary(tracker)
            elif choice == "2":
                amount = ask_amount("Withdrawal amount: ")
                note = input("Note (optional): ")
                add_transaction(tracker, -amount, note)
                save(tracker)
                show_summary(tracker)
            elif choice == "3":
                show_summary(tracker)
            elif choice == "4":
                show_history(tracker)
            elif choice == "5":
                tracker["goal"] = ask_amount("New goal: ")
                save(tracker)
                show_summary(tracker)
            elif choice == "6":
                print("Saved. See you next time!")
                break
            else:
                print("Please choose a number from 1 to 6.")
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
