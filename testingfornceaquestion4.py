"""this program will Prompt the user with: 'Enter a score, or type 'done' to exit: ', and keep collecting scores until 'done' is entered by the user. """

#constants and variables
SMART_SCORE = 80
FINISH_WORD = 'done'
#create an empty list
scores = []

#user input
score = input("Enter a score, or type 'done' to exit: ")

#loops
while score != FINISH_WORD:
    #check if score is valid
    try:
        score = int(score)
        if score >= 0:
            scores.append(score)
        else:
            print('Invalid score!')
    except ValueError:
        print('Invalid score!')
    #ask for more user input
    score = input("Enter a score, or type 'done' to exit: ")

#count the number of smart students
smart_students = 0
for score in scores:
    if score >= SMART_SCORE:
        smart_students += 1

#print the number of smart students
if smart_students == 1:
    print('This class has 1 smart student!')
else:
    print(f'this class has {smart_students} smart students!')