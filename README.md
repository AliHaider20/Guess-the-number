# Guess-the-number
User has to guess the number between 0 to 9
import random
n=random.randint(0,9)
guess=int(input("enter a number between 0 to 9:"))
print("")
def check(guess):
    while (guess!=n):
        if guess<n:
            print("The number  is  low")
            print("")
            guess=int(input("Enter once again"))
        elif guess>n:
            print("The number is  high")
            print("")
            guess=int(input("Enter once again"))
        
    print("you guessed it right")
check(guess)

