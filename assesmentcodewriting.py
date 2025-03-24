"""this program will detect whether certain speeds are unsafe"""

#variables
SAFE_SPEED = 10.0
FINISH_WORD = 'terminate'
ZERO = 0.0

#make an empty list to store speeds
safe_speeds = []
unsafe_speeds = []

#ask the user for input
speed = input('Input descent speed in m/s: ')

#loops and other code (add notation as needed)
while speed != FINISH_WORD:
    #check if speed is a number
    try:
        #convert speed to a float
        speed = float(speed)
        #check if speed is valid
        if speed >= ZERO:
            #check if speed is safe, and add to its respective list
            if speed > SAFE_SPEED:
                unsafe_speeds.append(speed)
            else:
                safe_speeds.append(speed)
        else:
            print('Error, invalid input.')
    except ValueError:
        print('Error, invalid input.')
    #ask for more user input
    speed = input('Input descent speed in m/s: ')

#final printing
print(f"There were {len(unsafe_speeds)} rockets faster than the safe speed.")
if len(unsafe_speeds) > 0:
    print('The unsafe speeds are')
    for num in unsafe_speeds:
        print(num)