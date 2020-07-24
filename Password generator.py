import random

#honestly had a hard time figuring out how to stay in the parameters of the challenge, so I improvised and made this mess
def badPassword():

    #making a couple lists to pull letters and symbols from in the loop to create the password
    listLet = list(range(65,91))
    for i in range(97,123):
        listLet.append(i)
    listSym = list(range(33,48))
    for i in range(58,65):
        listSym.append(i)
    for i in range(91,97):
        listSym.append(i)
    for i in range(123,127):
        listSym.append(i)

    password = ""
    while True:
        length = int(input("Enter the desired length of your password: "))
        letters = int(input("How many letters would you like in the password? "))
        num = int(input("How many numbers (The rest will be symbols)? "))
        if letters + num <= length:
            break
        else:
            print("You gave more numbers and letters than allows in specified length, please try again.")
            
    #loop that makes the password
    if letters != 0:
        for i in range(1,letters+1):
            asci = random.choice(listLet)
            char = chr(asci)
            password += char
    if num != 0:
        for i in range(1,num+1):
            char = str(random.randint(0,9))
            password += char
    for i in range(1,length - (num + letters)+1):
        asci = random.choice(listSym)
        char = chr(asci)
        password += char

    print(password)

#this is much shorter, and a more random password. Just has less customization options
def goodPassword():

    password = ""
    
    length = int(input("How long should the password be? "))
    for i in range(1,length + 1):
        asci = random.randint(33,126)
        char = chr(asci)
        password += char

    print(password)

#allows user to choose between the two generators
def main():
    print("You have two options:\nOne password generator is less efficient, weaker, but more customizable.\n\
The other is more efficient, stronger, but less customizable.")
    g = int(input("If you would like the first option, enter the interger one. For the other option, enter two: "))

    while g != 1 and g != 2:
        g = int(input("That is not a valid option, try again: "))

    if g == 1:
        badPassword()
    elif g == 2:
        goodPassword()

main()





        
            
