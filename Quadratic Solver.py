#Basic function to solve a quadratic equation in the form ax^2 + bx + c
#If x would be undefined, returns "n" instead of a value
import math
def solveQuad(a,b,c):
    test = ((b ** 2) - (4 * a * c))

    if test >= 0: #if the square root is define in the quadratic formula
        x = ((-b) + math.sqrt(test))/(2 * a)
        xN = ((-b) - math.sqrt(test))/(2 * a)
        print("The solutions of x for this quadratic equation are",x,"and",xN,end=".")
        
    else:
        print("The solution(s) for x are not defined.")

#allows user to repeatedly solve different quadratic equations
def main():

    print("This will solve a quadratic equation in the form ax^2 + bx + c. If one of these is missing, enter zero for the value.")
    repeat = "yes"
    
    while repeat == "yes":
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))
        solveQuad(a,b,c)

        repeat = input("Would you like to solve another equation? (yes/no): ").lower().strip()
        
main()
