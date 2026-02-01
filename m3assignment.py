import random;

# A conditional structure that evaluates at least two different possibilities and prints a meaningful result. For example, you might write code that assigns a letter grade based on a numeric score.
try:
    numGrade = float(input("Enter a numeric score (0-100): "))
    if numGrade >100 or numGrade <0:
        print('Sorry, you did not enter a valid numeric score (0-100).')
    else:
        letterGrade = '';
        if numGrade <=100 and numGrade >=90:
            letterGrade = 'A';
        elif numGrade <90 and numGrade >=80:
            letterGrade = 'B';
        elif numGrade <80 and numGrade >=70:
            letterGrade = 'C';
        elif numGrade <70 and numGrade >=60:
            letterGrade = 'D';
        elif numGrade <60 and numGrade >=0:
            letterGrade = 'F';
        print(f'Your letter grade is: {letterGrade}');
except:
    print ('Sorry, you did not enter a valid numeric score (0-100).')


# A for loop that processes a sequence such as a list of numbers, names, or strings and prints results in a clear format.
ingredients = ['white sugar', 'brown sugar', 'butter', 'chocolate chips', 'flour', 'vanilla', 'salt', 'eggs', 'baking soda']

print('\n\nHere is a list of ingredients needed to make chocolate chip cookies:');
for ingredient in ingredients:
    print(f'- {ingredient}')

print('\n\n')


# A while loop that continues until a condition is met, for example prompting the user until they guess the correct number or enter a valid password.

numberToGuess = int(random.randint(1,10))
userGuess = 0

while userGuess != numberToGuess:
    try:
        userGuess = int(input('Guess a number between 1 and 10: ' ))
        if userGuess != numberToGuess:
            print('Nope! Try again.')
    except: 
        print('Invalid input.')
 
print(f'Congrats! You guessed {numberToGuess} correctly.')
print('\n\n')

# At least one use of break or continue to demonstrate control inside a loop.

numberList = [5, 11, 2, 6, 1, 3]
numToFind = 6
print(numberList)
for index, i in enumerate(numberList):
    if i == numToFind:
        print(f'{i} was found at index {index}.')
        break;



