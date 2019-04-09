import random
print("Welcome to the number guessing geme!\nWhat's you name?")
userName= input()
print("well "+userName+" I'm thinking of a number between 10 and 20.")
guessToken=0
number= random.randint(10,20)

for guessToken in range(6):
    print("Take a guess")
    guessNumber=input()
    guessNumber=int(guessNumber)
    if guessNumber<number:
        print("your guess is too low")
    if guessNumber>number:
        print("your guess number is too high")
    if guessNumber==number:
        break

if guessNumber==number:
   guessToken=str(guessToken+1)
   print(userName+" you use "+guessToken+" to guess the correct number")