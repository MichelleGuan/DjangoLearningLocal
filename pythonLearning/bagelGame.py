import random
import math 

def Intro():
    print('Let\'s play a 2-4 digit number gussing game\nI will give you some clue each time you finish')

def ChooseDigit():
    digit = 0
    while digit not in range(1,11):
        print('How many digit would you like to play? (enter a number from 1-10)')
        digit = int(input())
    return digit

def RandomNumber(digit):
    startNumber = math.pow(10,digit-1)
    endNumber = math.pow(10,digit)-1
    randomNumber = random.randint(startNumber,endNumber)
    print(randomNumber)
    return randomNumber

def CheckNumber(randomNumber,inputNumber):
    totalCorrect = 0 
    partCorrect = 0 
    inputNumber = int(inputNumber)
    if inputNumber < randomNumber:
        print('Your guess is too low')
    elif inputNumber > randomNumber:
        print('Your guess is too high')
    else:
        print('You win')
        return
    inputNumber=str(inputNumber)
    randomNumber=str(randomNumber)
    for i in range(0,len(inputNumber)):
       if (inputNumber[i] == randomNumber[i]):
           totalCorrect += 1
       elif (inputNumber[i] in randomNumber):
           partCorrect +=1
    clue = 'You have '+str(totalCorrect)+' number totally correct\n'+str(partCorrect) +' number included but in different position'
    print(clue)

def GuessStart():
    playAgain = 'yes'
    while playAgain == 'yes':
        Intro()
        digit = ChooseDigit()
        ramdomNumber = RandomNumber(digit)
        for i in range(6):
            print('You can guess now')
            inputNumber = input()
            if len(inputNumber) == digit:
                CheckNumber(ramdomNumber,inputNumber)
            if inputNumber[0] == '0':
                print('You can\'t put 0 in front of number')
            else:
                print('digit is not corret')
        print('Times out! Do you want to play again? (yes or no)')
        playAgain=input()

GuessStart()