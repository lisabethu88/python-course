"""
data_handling.py

Handles user input and formatted output for the budgeting program.
This module separates input/output logic from calculation logic.
"""

import ast
import locale

# Ask user to enter monthly after-tax income
def getIncome():
    """
    Prompt the user to enter their monthly after-tax income.

    Repeats the prompt until the user enters a valid numeric value
    (int or float).

    Returns:
        int or float: The validated monthly income entered by the user.
    """
    isValid = False
    while not isValid:
        try:
            income = ast.literal_eval(input("What is your monthly after-tax income?: $"))
        except:
            print("Error: Please enter in a valid income.")
        else:
            isValid = isinstance(income, float ) or isinstance(income, int)
            if not isValid:
                print("Error: Please enter in a valid income.")
            else:
                return income

# print output
def printOutput(budgetDict):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    for key, value in budgetDict.items():
        print(f'{key}: {locale.currency(value, grouping=True)}')