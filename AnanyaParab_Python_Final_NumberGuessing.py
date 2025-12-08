#imports the random library
import random


name = input("Welcome to the number guessing game! Enter your name here: ")
print(f"Hi {name}! Let's begin the game")

#only for testing, lets me see number to make sure the if-elif-else is working 
#random.seed(50)
secret = random.randint(1, 100)
#print(secret)

#lets user pick a number
guess = int(input("Guess a number between 1-100: "))
#keeps count of how many times someone guesses
count = 0
score = 100

#looks at how far away the guess is from the acutal number. this is the hot and cold system
while guess != secret:
    #sees if guess is in the same decade (ex. 77 is in the '70s')
    if (guess // 10) == (secret // 10):
        print("Your guess was in the same decade as the secret number!")
        guess = int(input("Guess again: "))
        count += 1
        score -= 7
    elif (abs(guess - secret)) < 6:
        print("Extremely hot! But not quite correct")
        guess = int(input("Guess again: "))
        count += 1
        score -= 7
    elif (abs(guess - secret)) < 11:
        print("Hot! Your number is getting close.")
        guess = int(input("Guess again: "))
        count += 1
        score -= 7
    elif (abs(guess - secret)) < 21:
        print("Your guess was warm.")
        guess = int(input("Guess again: "))
        count += 1
        score -= 7
    elif (abs(guess - secret)) < 41:
        print("Cold! Try again!")
        guess = int(input("Guess again: "))
        count += 1
        score -= 7
    else:
        print("Freezing. Is it getting colder in here?")
        guess = int(input("Guess again: "))
        count += 1
        score -= 7
#checks if guess if correct, and the following protocol
if guess == secret:
    #scoring correctly gives u 5 more points
    score += 5
    count += 1
    print(f"Your guess was correct! it only took you {count} tries")
    if score >= 70:
        print(f"Your score was {score}, which is greater than 70, so if this was a test you would have passed!")
    else:
        print(f"Your score was {score}, which is less than 70, so if this was a test you would have failed :C)")
print("Thanks for playing!")