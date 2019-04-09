import random
import time
def displayIntro():
    print("You are in land full of dragons. You see two caves infront of you." 
           +"In one cave there's a treasure box whereas the other remains a hungry dragon")

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' :
        time.sleep(1)
        print('which cave will you choose? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosen):
    treasure = random.randint(1,2)
    print('you are approaching the terminal')
    time.sleep(2)
    if chosen == treasure:
        print("congradulations")
    else:
        print("sorry")  

def playNext():
    playAgain='yes'
    while playAgain == 'yes':
        displayIntro()
        chosen=int(chooseCave())
        checkCave(chosen)
        print('Do you want to play again? (yes or no)')
        playAgain=input()

playNext()