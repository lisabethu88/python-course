# variables
num1 = 5
num2 = 10
num3 = 15
num4= 20
string1 = "Hello, my name is Lisa"
string2 = "and I love dogs!"
bool1 = False
bool2 = True

# arithmetic operations
quotient = int(num2 / num1 )
sum = num4 + num3
difference = num4 - num1
product = num3 * num2
expression = (product * difference) + sum**quotient

print(f'{num2} / {num1} = {quotient}')
print(f'{num4} + {num3} = {sum}')
print(f'{num4} - {num1} = {difference}')
print(f'{num3} * {num2} = {product}')
print(f'({product} * {difference}) + {sum} ** {quotient} = {expression}')

# string operations
stringSlice = string1[0:5]
print(stringSlice)
stringConcatenated = string1 + ' ' + string2
print(stringConcatenated)
stringFormatted = f'{stringConcatenated[0:28]} have {num1 - 2} pets.'
print(stringFormatted)

# boolean operations
print(f'Question: True or False? {num1} > {num2} \n Answer: {num1 > num2}')