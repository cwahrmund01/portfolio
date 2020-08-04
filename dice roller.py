import random

#all of the different functions to roll different sized dice use the same formula, jonly one digit needs to be changed
def d20(rolls):

    rollsList = []
    total = 0
    for i in range(1,rolls + 1):
        current = random.randint(1,20)
        rollsList.append(current)
        total += current

    print("The rolls were:",end=" ")
    for roll in rollsList:
        print(roll,end=" ")
    print("   For a total of:",total)

def d12(rolls):

    rollsList = []
    total = 0
    for i in range(1,rolls + 1):
        current = random.randint(1,12)
        rollsList.append(current)
        total += current

    print("The rolls were:",end=" ")
    for roll in rollsList:
        print(roll,end=" ")
    print("   For a total of:",total)


def d10(rolls):

    rollsList = []
    total = 0
    for i in range(1,rolls + 1):
        current = random.randint(1,10)
        rollsList.append(current)
        total += current

    print("The rolls were:",end=" ")
    for roll in rollsList:
        print(roll,end=" ")
    print("   For a total of:",total)

def d8(rolls):

    rollsList = []
    total = 0
    for i in range(1,rolls + 1):
        current = random.randint(1,8)
        rollsList.append(current)
        total += current

    print("The rolls were:",end=" ")
    for roll in rollsList:
        print(roll,end=" ")
    print("   For a total of:",total)

def d6(rolls):

    rollsList = []
    total = 0
    for i in range(1,rolls + 1):
        current = random.randint(1,6)
        rollsList.append(current)
        total += current

    print("The rolls were:",end=" ")
    for roll in rollsList:
        print(roll,end=" ")
    print("   For a total of:",total)

def d4(rolls):

    rollsList = []
    total = 0
    for i in range(1,rolls + 1):
        current = random.randint(1,4)
        rollsList.append(current)
        total += current

    print("The rolls were:",end=" ")
    for roll in rollsList:
        print(roll,end=" ")
    print("   For a total of:",total)

#main() allows the user to type easier to understand strings (2d20 instead of d20(2)) to make the program more user friendly
def main():

    rollAgain = "yes"
    
    while rollAgain == "yes":
            
        startState = input("Enter your desired number of rolls followed by the dice wanted (ex: 2d20 would roll 2 20-sided dice): ").lower().strip()
        print(startState)

        splitState = []
        for a in startState:
            splitState.append(a)
        print(splitState)

        #determines how many times to roll the dice
        if splitState[0].isdigit() and splitState[1].isdigit():
            rolls = int(splitState[0]) * 10 + int(splitState[1])
            if splitState[2].isalpha: #this just continues to confirm the correct format was used as to not confuse the program
                #determines which dice to roll
                if splitState[3] == "2" and splitState[4] == "0" and len(splitState) == 5:
                    d20(rolls)
                elif splitState[3] == "1" and splitState[4] == "2" and len(splitState) == 5:
                    d12(rolls)
                elif splitState[3] == "1" and splitState[4] == "0" and len(splitState) == 5:
                    d10(rolls)
                elif splitState[3] == "8" and len(splitState) == 4:
                    d8(rolls)
                elif splitState[3] == "6" and len(splitState) == 4:
                    d6(rolls)
                elif splitState[3] == "4" and len(splitState) == 4:
                    d4(rolls)
                else:
                    print("The format seems to be off in some way, make sure it looks something like 2d20 or 12d6.")

            else: #if there is no d or really any letter (just in case of a small typo) after the first two digits
                print("The format seems to be off in some way, make sure it looks something like 2d20 or 12d6.")

        elif splitState[0].isdigit() and not splitState[1].isdigit():
            rolls = int(splitState[0])
            if splitState[1].isalpha():
                #determines which dice to roll
                if splitState[2] == "2" and splitState[3] == "0" and len(splitState) == 4:
                    d20(rolls)
                elif splitState[2] == "1" and splitState[3] == "2" and len(splitState) == 4:
                    d12(rolls)
                elif splitState[2] == "1" and splitState[3] == "0" and len(splitState) == 4:
                    d10(rolls)
                elif splitState[2] == "8" and len(splitState) == 3:
                    d8(rolls)
                elif splitState[2] == "6" and len(splitState) == 3:
                    d6(rolls)
                elif splitState[2] == "4" and len(splitState) == 3:
                    d4(rolls)
                else:
                    print("The format seems to be off in some way, make sure it looks something like 2d20 or 12d6.")
                    
            else:
                print("The format seems to be off in some way, make sure it looks something like 2d20 or 12d6.")

            
        else:
            print("The first character must be a number, 1-99 included, to say how many times you want to roll the specified dice.")

        rollAgain = input("Would you like to roll another set of dice (yes/no)? ").lower().strip()
main()
    
