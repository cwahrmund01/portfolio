import random

def main():

    #Setting up target number and original guess
    answer = random.randint(1,20)
    guess = int(input("Guess a number from 1 to 20 (20 included): "))

    #Loop that receives a new answer until the correct answer is guessed
    #Also tells the user whether the guess is too low/high
    while guess != answer:

        if guess > answer:
            guess = int(input("That guess was too high, try again: "))
        elif guess < answer:
            guess = int(input("That guess was too low, try again: "))

    print("That guess was correct, good job!")

main()
