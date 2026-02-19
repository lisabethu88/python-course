"""
budget_calculations.py

Contains functions that implement the 50/30/20 budgeting rule.
This module is responsible for all income allocation calculations.
"""


def calcBudget(income=0):
    """
    Calculate a 50/30/20 budget breakdown based on income.

    Uses the 50/30/20 budgeting rule to divide the given income into:
        - 50% for Needs
        - 30% for Wants
        - 20% for Savings

    Args:
        income (int | float, optional): Monthly after-tax income.
                                        Defaults to 0.

    Returns:
        dict: A dictionary containing the calculated budget allocation
              with keys 'Needs', 'Wants', and 'Savings'.
    """
    needs = calcNeeds(income)
    wants = calcWants(income)
    savings = calcSavings(income)
    budgetDict = {
        "Needs": needs, "Wants": wants, "Savings": savings
    }
    return budgetDict
    
def calcNeeds(income=0):
    """
    Calculate the portion of income allocated to Needs.

    Allocates 50% of the provided income according to
    the 50/30/20 budgeting rule.

    Args:
        income (int | float, optional): Monthly after-tax income.
                                        Defaults to 0.

    Returns:
        float: The amount put towards Needs.
    """
    return 0.5 * income

def calcWants(income=0):
    """
    Calculate the portion of income allocated to Wants.

    Allocates 30% of the provided income according to
    the 50/30/20 budgeting rule.

    Args:
        income (int | float, optional): Monthly after-tax income.
                                        Defaults to 0.

    Returns:
        float: The amount put towards Wants.
    """
    return 0.3 * income

def calcSavings(income=0):
    """
    Calculate the portion of income allocated to Savings.

    Allocates 20% of the provided income according to
    the 50/30/20 budgeting rule.

    Args:
        income (int | float, optional): Monthly after-tax income.
                                        Defaults to 0.

    Returns:
        float: The amount put towards Savings.
    """
    return 0.2 * income