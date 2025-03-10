name = input('What is your name? ')
print(f'Hello {name}, nice to meet you!')
age = int(input(f'How old are you {name}? '))

if age == 15:
    print('Great age!')
elif age < 10:
    print('Why are you so young?')
elif age > 100:
    print("You have to be lying. There's no way you're that old.")
else:
    print('cool!')