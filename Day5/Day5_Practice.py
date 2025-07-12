#Oriana J.

#Day 5 Tasks

#1. Create a custom module file named `calculator.py` that defines functions:
#   - `add(x, y)`
#   - `subtract(x, y)`
#   - `multiply(x, y)`
#   - `divide(x, y)` (handle division by zero)


#2. In a separate script, import your `calculator` module.

#3. Build a menu-driven program:
#   - Ask the user for an operation: +, -, *, /
#   - Ask for two numbers
#   - Use the corresponding function from your module
#   - Print the result or an error message for invalid inputs

import calculator
print("Welcome user to a basic Python Calculator ")
print (" ")

operation = input(" Choose an Operation ( +, -, *, /): ")

num1 = float(input("Enter the first number: "))

if operation == '/':
     while True:
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Invalid, cannot divide by zero. Enter again: ")
        else:
            answer = calculator.division(num1,num2)
            break


else:
    num2 = float(input("Enter the second number: "))
    
    if operation == '+':
        answer = calculator.add(num1,num2)
    elif operation == '-':
        answer = calculator.subtract(num1,num2)
    elif operation == '*':
        answer = calculator.multiplication(num1,num2)
    else:
        answer = None

if answer is not None:
    print("Answer: ", answer)

else:
    print ("Invalid")


#-----------------Expected output--------------#

    ##Addition
    
    ##Choose an Operation ( +, -, *, /): +
    ##Enter the first number: 30
    ##Enter the second number: 20
    ##Answer:  50.0


    ##Subtraction
    ##Choose an Operation ( +, -, *, /): -
    ##Enter the first number: 100
    ##Enter the second number: 25
    ##Answer:  75.0

    ##Choose an Operation ( +, -, *, /): /
    ##Enter the first number: 50
    ##Enter the second number: 5
    ##Answer:  10.0


    

    











