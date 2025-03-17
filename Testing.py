"""this program will do stuff"""

#variables
MINIMUM = 34
MAXIMUM = 42
temperatures = []
end = -1
variable_idk = int(input('Enter the temperature: '))

#loops and other code
while variable_idk != end:
  temperatures.append(variable_idk)
  variable_idk = int(input('Enter the temperature: '))

#final printing
for temps in temperatures:
  if temps < MINIMUM:
    print("too cold")
  elif temps > MAXIMUM:
    print("too hot")
  else:
    print("just right")