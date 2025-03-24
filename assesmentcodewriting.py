"""this program will detect whether certain speeds are unsafe"""

#variables
SAFE_SPEED = 10.0
FINISH_WORD = 'terminate'
ZERO = 0

#make an empty list to store speeds
safe_speeds = []
unsafe_speeds = []

#ask the user for input
speed = input('Input descent speed in m/s: ')

#loops and other code (add notation as needed)
while speed != FINISH_WORD:
    #check if speed is a number
    try:
        #convert speed from a string to a float
        speed = float(speed)
        #check if speed is a valid number
        if speed >= ZERO:
             #check if speed is faster than safe speed
             if speed > SAFE_SPEED:
                #add speed to unsafe_speeds
                unsafe_speeds.append(speed)
            else:
                #add speed to safe_speeds
                safe_speeds.append(speed)
        else:
            #if speed is a negative number, then print this message
            print('Error, invalid input.')
    except ValueError:
        #if speed is not a number, then print this message
        print('Error, invalid input.')

#final printing / code ending
