""" This Program will ask the amount spent, then when the number 0 is reached
     or the number 0 is inputted into the program, it will print out all of the
     bank balances that the user reached, in order."""

STARTING_BALANCE = 200
changing_balance = 200

#open an empty list, for the purpose of storing the inputs
balances = []

#input the amounts spent until the requirements are reached for an ending
while True:
    try:
        #ask the user to input the amount spent
        spent = int(input('Enter the amount spent: '))
        #check if the input is valid
        if spent >= 0:
          #check for end requirement 1
          if spent <= 0:
              break
          #minus the 'spent' amount from the starting balance, and save it as a new balance
          result = changing_balance - spent
          #add changing balance to balances, and update changing balance to match result
          changing_balance = result
          balances.append(changing_balance)
          #check for end requirements
          if changing_balance <= 0:
              break
        else:
            print('That is not a valid transaction.')
    except ValueError:
        print('That is not a valid transaction.')

#final printing
print('My bank balances have been:')
print(STARTING_BALANCE)
#repeat for every balance in balances
for balance in balances:
    print(balance)