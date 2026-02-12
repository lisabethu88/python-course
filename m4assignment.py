
def add(num1, num2):
    """
    Adds two num values and returns the sum.

    If the result is a whole number, it is returned as an int.
    Otherwise, it is returned as a float.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        int or float: The sum of num1 and num2.
    """
    sum = num1 + num2
    if sum.is_integer():
        sum = int(sum)
    return sum

def multiply(num1, num2):
    """
    Multiplies two num values and returns the product.

    If the result is a whole number, it is returned as an int.
    Otherwise, it is returned as a float.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        int or float: The product of num1 and num2.
    """
    product = num1 * num2
    if product.is_integer():
        product = int(product)
    return product
    

def divide(num1, num2):
    """
    Divides two num values and returns the quotient.

    Try/except handles Division By Zero error. If error is caught, the function prints an error message and exits.

    If the result is a whole number, it is returned as an int.
    Otherwise, it is returned as a float.

    Parameters:
        num1 (float): The first number (dividend).
        num2 (float): The second number (divisor).

    Returns:
        int or float: The quotient of num1 and num2.
    """
    try:
        quotient = num1 / num2
        if quotient.is_integer():
            quotient = int(quotient)
        return quotient
    except ZeroDivisionError:
        print("ERROR: Cannot divide by 0.")

def sub(num1, num2):
    """
    Subtracts two num values and returns the difference.

    If the result is a whole number, it is returned as an int.
    Otherwise, it is returned as a float.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        int or float: The sum of num1 and num2.
    """
    diff = num1 - num2
    if diff.is_integer():
        diff = int(diff)
    return diff

def get_float(prompt):
    """
    Asks the user to input a number.

    Try/except handles ValueError. If user does not input a number, an error message is printed.

    Parameters:
        prompt (string): User prompt.

    Returns:
        float: The number the user put in. 
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("ERROR: Invalid number. Please try again!")

def get_operator(operators=None):
    """
    Asks the user to input a character representing an operator.

    If input is not a character found in the operators list, the function repeatedly prompts the user for a valid operator.

    Parameters:
        operators (list): A list of calid operators, default is None.

    Returns:
        op: The operator the user put in. 
    """
    if operators is None:
        operators = ['/', '*', '+', '-']
    while True:
        op = input("Enter Operator (options: +, -, *, /): ")
        if op in operators:
            return op
        print("ERROR: Invalid operator. Please try again!")

def getUserInput():
    """
    Calls getFloat and getOperator functions to gather user input. 

    Parameters:
        None.

    Returns:
        A list containing a number, the operator, and a second number from user input in that exact order.
    """
    first = get_float("Enter First Number: ")
    operator = get_operator()
    second = get_float("Enter Second Number: ")
    return [first, operator, second]

print('--------------')
print('Calculator App')
print('--------------')

userInput = getUserInput();

if userInput[1] == '+':
    result = add(userInput[0], userInput[2])
elif userInput[1] == '-':
    result = sub(userInput[0], userInput[2])
elif userInput[1] == '*':
    result = multiply(userInput[0], userInput[2])
elif userInput[1] == '/':
    result = divide(userInput[0], userInput[2])

if result:
    print(f'Result: {result}' )


x = 10  # global

def test_scope():
    """
    Demonstrates scope by printing a local variable.

    Parameters:
        None.

    Returns:
        Nothing.
    """
    x = 5  # local
    print("Inside function:", x)

test_scope()
print("Outside function:", x)