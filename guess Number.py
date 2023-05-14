import random

num = random.randint(1, 100)
guess = 0

while guess != num:
    guess = input("guess a number between 1 and 100: ")
    guess = int(guess)
    if guess == num:
        print("you guess currect!")
        break
    elif guess > num:
        print("you guess is higher!")
      
    else :
        print("you guess is lower!")
 
   