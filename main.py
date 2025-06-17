"""
    Initial setup - June 17th 2025 0830
    Python Calculator Project
        Basic arethemitic functions (add, subtract, multiply, divide)
"""

"""
    1.) Ask the user what they would like to do.
    2.) Ask the user for 2 variables.
    3.) Preform selected operation with variables from step 2.
    4.) Display the result to the user.
    5.) Ask the user if they would like to run the program again (Optional).
"""

print("Please select an operation")
print("A - Addition")
print("S - Subtraction")
print("M - Multiplication")
print("D - Division")

userChoice = input("Welcome, what operation would you like to perform: ")
print(userChoice)

if userChoice == "A" or userChoice == "a":
    stringX = input("Please enter a number for x: ")
    integerX = int(stringX)
    
    stringY = input("Please enter a number for y: ")
    integerY = int(stringY)

    result = integerX + integerY
    print(result)

elif userChoice == "S" or userChoice == "s":
    stringX = input("Please enter a number for x: ")
    integerX = int(stringX)
    
    stringY = input("Please enter a number for y: ")
    integerY = int(stringY)

    result = integerX - integerY
    print(result)

elif userChoice == "M" or userChoice == "m":
    stringX = input("Please enter a number for x: ")
    integerX = int(stringX)
    
    stringY = input("Please enter a number for y: ")
    integerY = int(stringY)

    result = integerX * integerY
    print(result)