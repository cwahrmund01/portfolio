#This is my hangman game. This is going to be mostly practice and proof of concept so the list of possible words
#won't be massive, but it will serve its purpose
#I am still learning string manipulations, so this game only works if a letter appears a maximum of two times

import random

def hangMan(answer):
    
    #beginning variables to track guesses, and how many wrong guesses have been made
    tracker = ["_"]*len(answer)
    guesses = []
    wGuesses = 0
    wGuessesL = []
    
    #Loops until counter that counts wrong guesses reaches 6
    while wGuesses != 6:
        guess = input("Please enter the letter that you guess: ").lower().strip()

        #this makes sure that invalid guesses do not count against the user
        while len(guess) != 1:
            guess = input("That is an invalid guess (not a letter or more than one letter). Try agin: ").lower().strip()

        #makes sure repeat guesses do not count against the user
        while guess in guesses:
            guess = input("You have already guessed that letter, guess another: ").lower().strip()   
        guesses.append(guess)

        #The part that checks whether the guess is right, and updates the tracker/wrong guesses counter
        if guess in answer:
            numIn = answer.count(guess)

            if numIn == 1: #if letter occurs once, only need to find the index of one letter
                location = answer.find(guess)
                tracker[location] = guess

            elif numIn == 2: #if letter occurs twice, need to do find and rfind to find both positions
                lLocation = answer.find(guess)
                rLocation = answer.rfind(guess)
                tracker[lLocation] = guess
                tracker[rLocation] = guess

        else: #if guess is not in the answer, adds to wGuesses counter and adds to wrong guesses list
            wGuessesL.append(guess)
            wGuesses += 1

        #prints the tracker for the user with any letters they've guessed correctly so far filled in
        for a in tracker:
            print(a,end=" ")
        print("")

        #shows the wrong guesses so far
        if (len(wGuessesL) != 0) and ("_" in tracker):
            print("Wrong guesses so far: ", end="")
            for a in wGuessesL:
                print(a, end=" ")
            print("")

        #ends the program if the tracker gets filled, and has a special ending if no wrong guesses were made
        if "_" not in tracker and len(wGuessesL) == 0:
            print("Congratulations, you guessed the word without any mistakes!")
            return
        elif "_" not in tracker:
            print("Congratulations, you guessed the word!")
            return

    #if loop ends (6 wrong guesses occur) then the game ends and shows the user the correct answer
    print("You ran out of guesses. The word was",answer)

#this is mainly for the user confirmation loop, but also allows me to easily add new words
def main():

    listWords = ["apple","nostalgia","program","tundra","capital","fifty","question","orange","phone","clean","yesterday","food","stormy","keyboard","picture"]
    play = "yes"
    print("This is the game Hangman. You will get 6 guesses before you lose. Good luck!")
    
    while play == "yes":
        
        word = random.choice(listWords)
        hangMan(word)

        play = input("Would you like to play again? (yes/no): ").lower().strip()
    
main()
