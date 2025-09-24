import random
num=random.randint(1,100)
attempts=0
max_attempts=5
print("Welcome to the number guessing game!") 
print("You have to guess a number between 1 and 100")
print("You have 5 attempts")
guess=int(input("Enter a nummber between 1 and 100"))
while attempts<max_attempts:
    guess=int(input("Guess the number:"))
    attempts+=1
if guess==num:
    print("Win")
elif guess<num:
    print("Too low")
elif guess>num:
    print("Too high")
else:
    print("Lose")

