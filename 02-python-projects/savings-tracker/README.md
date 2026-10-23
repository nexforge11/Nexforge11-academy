# Savings Tracker

A command-line savings tracker. It grows the Lesson 01 mini project
([`mini_project_savings_tracker.ipynb`](../../mini_project_savings_tracker.ipynb)) into a small program that is
interactive and saves your data between runs.

## What it does
- Set a savings goal
- Add deposits and withdrawals, with an optional note
- Show how much you've saved, how much is left, and a progress bar
- List every transaction you've made
- Save everything to `savings_data.json` so it's still there next time

```
Goal:      200.00
Saved:     80.00
Remaining: 120.00
[########------------] 40.0%
```

## How to run it
```
cd 02-python-projects/savings-tracker
python savings_tracker.py
```

**In Google Colab:** upload `savings_tracker.py`, then in a cell run `!python savings_tracker.py`,
or paste the file's contents into a cell and run it. The `input()` prompts work in Colab.

## How to run the tests
```
python -m unittest test_savings_tracker.py
```

## Concepts used
| Concept | Where to look |
|---|---|
| Functions | `balance()`, `remaining()`, `progress_percent()` |
| Dictionaries and lists | The tracker is a dict holding a list of transactions |
| Loops | `balance()` adds up the transactions; `main()` repeats the menu |
| Conditionals | Menu choices in `main()`, the checks in `add_transaction()` |
| Error handling | `ask_amount()` uses `try`/`except` to reject anything that isn't a number |
| Files and JSON | `save()` and `load()` |
| Testing | `test_savings_tracker.py` |

## Practice ideas: try these yourself
1. Show the average deposit amount in the summary.
2. Add a menu option that deletes the last transaction.
3. Estimate how many more deposits of a given size are needed to reach the goal.
4. Support more than one goal, e.g. "Laptop" and "Holiday".

Write a test for each new feature before you call it finished.

**Privacy:** `savings_data.json` contains your own figures, so it is listed in `.gitignore` and won't be committed.
