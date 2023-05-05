# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
        #Double indentions caused an unexpected indent error
        #while cave != '1' and cave != '2':
    while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()
    #nothing is being returned here because caves is not defined. IF   we change it to cave it'll identify the formula and return the cave leading to the code to function properly.
    #return caves
    #Correct code is here
    return cave
    #what you want to do is type in return cave
def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        #The call to print is missing parentheses and when you add in parentheses then the print function will print the message.
        #print 'Gobbles you down in one bite!'
        #print ('Gobbles you down in one bite!') will proceed to print the message
        print ('Gobbles you down in one bite!')


displayIntro()
#choosecave is undefined because of the lower C in cave. If you turn it to uppercase to identify it from line 18, it will fix the code
#caveNumber = choosecave()
#type in caveNumber = chooseCave() instead to have it properly identify line 18
caveNumber = chooseCave()
checkCave(caveNumber)
    
print("Thanks for playing")