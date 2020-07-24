import random

def main():

    yn = "yes"
    #Allows the player to play again, or escape the game if they would like
    while yn == "yes":

        #Sets computer's choice and receives player choice
        cpuChoice = random.choice(["rock","paper","scissors"])
        pcChoice = input("Choose rock, paper, or scissors: ").lower().strip()

        #ensures player choice is a valid choice that the game will recognize
        while True:
            if pcChoice == "rock" or pcChoice == "scissors" or pcChoice == "paper":
                break
            else:
                pcChoice = input("That choice is not a valid choice. Choose rock, paper, or scissors: ").lower().strip()

        #if/elif/else statements that determine who won, or if there was a tie
        if cpuChoice == "rock":
            if pcChoice == "scissors":
                print("You lost. The computer chose",cpuChoice,"and",cpuChoice,"beats",pcChoice,end=".")
            elif pcChoice == "paper":
                print("You won! The computer chose",cpuChoice,"and",pcChoice,"beats",cpuChoice,end=".")
            else:
                print("It's a tie! Both you and the computer chose",cpuChoice,end=".")
        elif cpuChoice == "paper":
            if pcChoice == "rock":
                print("You lost. The computer chose",cpuChoice,"and",cpuChoice,"beats",pcChoice,end=".")
            elif pcChoice == "scissors":
                print("You won! The computer chose",cpuChoice,"and",pcChoice,"beats",cpuChoice,end=".")
            else:
                print("It's a tie! Both you and the computer chose",cpuChoice,end=".")
        else:
            if pcChoice == "paper":
                print("You lost. The computer chose",cpuChoice,"and",cpuChoice,"beats",pcChoice,end=".")
            elif pcChoice == "rock":
                print("You won! The computer chose",cpuChoice,"and",pcChoice,"beats",cpuChoice,end=".")
            else:
                print("It's a tie! Both you and the computer chose",cpuChoice,end=".")
        
        #does the player want to play again?
        yn = input("\nWould you like to play again? Yes/No: ").lower().strip()


main()
