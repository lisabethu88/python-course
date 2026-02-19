import tools.data_handling as data
from tools.budget_calculations import calcBudget

def printWelcomeMessage():
    """
    Display the program welcome message and explanation.

    Prints a formatted header along with a brief description of the
    Budget Calculator and an explanation of the 50/30/20 budgeting rule,
    which divides up your income toward Needs (50%), Wants (30%), and Savings (20%).

    Returns:
        None
    """
    print("=================")
    print('Budget Calculator')
    print("=================")
    print('This calculator creates a budget based on your take-home pay with the 50/30/20 rule.')
    print('The 50/30/20 rule states that you should put 50% of your income towards Needs, 30% towards Wants, and 20% towards Savings.')
    print('\n')

printWelcomeMessage()
income = data.getIncome()
budgetDict = calcBudget(income)
data.printOutput(budgetDict)
