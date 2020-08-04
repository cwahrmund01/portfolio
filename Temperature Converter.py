#Basic temperature converter, can convert F, C, and K to either of the other two based on user needs.

def main():

    print("This will convert your temperature between Celsius, Kelvin, and Fahrenheit.")
    #receives needed info from user
    value = float(input("Enter the value of your temperature (the number): "))
    typ = input("What scale is your temperature in? (Kelvin(K), Celsius(C), or Fahrenheit(F)): ").lower().strip()
    desiredType = input("What temperature scale would you like to conver to (same options as above): ").lower().strip()

    #if original scale is Kelvin
    if typ == "k" or typ == "kelvin":
        if desiredType == "k" or desiredType == "kelvin":
            print("It's the same temperature scale as the original.")
        elif desiredType == "c" or desiredType == "celsius":
            newValue = round(value - 273.15,3)
            print(value,"Kelvin is equivalent to",newValue,"degrees Celsius.")
        elif desiredType == "f" or desiredType == "fahrenheit":
            newValue = round((9/5) * (value - 273.15) + 32,3)
            print(value,"Kelvin is equivalent to",newValue,"degrees Fahrenheit.")
        else:#if desiredType is not recognized
            again = input("There was some typo in the scale you wanted to convert to, would you like to try again? (yes/no): ")\
            .lower().strip()
            if again == "yes":
                main()
    #if original scale is Celsius
    elif typ == "c" or typ == "celsius":
        if desiredType == "c" or desiredType == "celsius":
            print("It's the same temperature scale as the original.")
        elif desiredType == "k" or desiredType == "kelvin":
            newValue = round(value + 273.15,3)
            print(value,"degrees Celsius is equivalent to",newValue,"Kelvin.")
        elif desiredType == "f" or desiredType == "fahrenheit":
            newValue = round((9/5) * value + 32,3)
            print(value,"degrees Celsius is equivalent to",newValue,"degrees Fahrenheit.")
        else:#if desiredType is not recognized
            again = input("There was some typo in the scale you wanted to convert to, would you like to try again? (yes/no): ")\
            .lower().strip()
            if again == "yes":
                main()
    #if original scale is Fahrenheit
    elif typ == "f" or typ == "fahrenheit":
        if desiredType == "f" or desiredType == "fahrenheit":
            print("It's the same temperature scale as the original.")
        elif desiredType == "k" or desiredType == "kelvin":
            newValue = round((5/9) * (value - 32) + 273.15,3)
            print(value,"degrees Fahrenheit is equivalent to",newValue,"Kelvin.")
        elif desiredType == "c" or desiredType == "celsius":
            newValue = round((5/9) * (value - 32),3)
            print(value,"degrees Fahrenheit is equivalent to",newValue,"degrees Celsius.")
        else:#if desiredType is not recognized
            again = input("There was some typo in the scale you wanted to convert to, would you like to try again? (yes/no): ")\
            .lower().strip()
            if again == "yes":
                main()

    else: #if the original scale entered is not recognized
        again = input("There was some typo in your original temperature scale, would you like to try again? (yes/no): ")\
            .lower().strip()
        if again == "yes":
            main()

main()
