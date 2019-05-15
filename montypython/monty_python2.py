#!/usr/bin/env python3

round = 0 # integer round initiated to 0
while(True): # sets up an infinate loop condition
    round = round + 1 # increase round counter
    print('Finish the movie title, "Monty Python\'s The life of ______"')
    answer = input() # string answer collected from user
    if (answer == 'Brian'): # logic to check if the user gave correct answer
        print("Correct")
        break # break statement escapes the while loop
    elif (round==3): # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
        break # break statement escapes the while loop
    else: # if answer is wrong, and round has not yet equal 3
        print("Sorry! Try again!")
