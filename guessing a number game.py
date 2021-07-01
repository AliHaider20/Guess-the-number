import random
n=random.randint(0,9)
guess=int(input("enter a number between 0 to 9:\n"))
def check(guess):
   guesses = 3
   while (guess!=n and guesses!=0):
      if guess<n:
         print("The number  is  low")
         print(f"{guesses} guesses are left\n")
         guess=int(input("Enter once again"))
      elif guess>n:
         print("The number is  high")
         print(f"{guesses} guesses are left\n")
         guess=int(input("Enter once again"))
      guesses-=1
   print("Hurray! You guessed it right")

if __name__ == "__main__":
   check(guess)
