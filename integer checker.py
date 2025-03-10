""" This program will check to see if the user has entered a valid integer 
    in a specific range of values """

#use constants for the low and high values
LOWEST = 1
HIGHEST = 10

#ask the user to type in a number
number = input('Please enter an integer: ')

#check to see if the number is valid
if number.lstrip('-').isnumeric():
    number = int(number)
    if number < LOWEST:
      print(f"Your number is lower than {LOWEST}")
    elif number > HIGHEST:
      print(f"Your number is greater than {HIGHEST}")
    else:
        print(f"Your number is {number}")
else:
    print(f"{number} is not an integer")