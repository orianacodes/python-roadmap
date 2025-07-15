# Oriana J.

#Day 6 Practice

#Tasks 
#Write a function called cube that returns the cube of a number.
#Write a function multiply that takes two numbers and returns the result.
#Write a function max_number that takes two numbers and returns the larger one.
#Call the functions and print their results.

#---------------------------------------------------------------------#

#Write a function called cube that returns the cube of a number.
def cube(number):
    return (number * number * number)

#Write a function multiply that takes two numbers and returns the result.
def multiply (num1, num2):
    return num1 * num2

#Write a function max_number that takes two numbers and returns the larger
#one.

def max_number (n1,n2):
    
    if n1 > n2:
        return n1
    elif n1 == n2:
        return n1
    else:
        return n2

    #Call the functions and print their results.

cube_num = cube(2)
print ("Cube of 2: ", cube_num)


product = multiply (5,5)
print("Multiplication of 5 and 5: ", product)

largest = max_number(9,12)
print("Larger number between 9 and 12: ", largest)

#OUTPUT
#Cube of 2:  8
#Multiplication of 5 and 5:  25
#Larger number between 9 and 12:  12





    

    
    







































