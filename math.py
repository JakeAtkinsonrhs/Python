"""this program will ask the user for their name and favourite numbers
and then form some simple maths on the numbers"""

# Ask the user for their name and favourite numbers
name = input('What is your name? ')
number1 = int(input('What is your favourite number? '))
number2 = int(input('What is your second favourite number? '))

# addition and multiplication
add = number1 + number2
multiply = number1 * number2

#greet the user and print the results
print(f'Hi {name}, here are some fun calculations with your favourite numbers.')
print(f'{number1} + {number2} = {add}')
print(f'{number1} * {number2} = {multiply}')