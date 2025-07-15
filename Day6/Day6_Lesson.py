#Oriana J.

#Day 6: Functions with Return Values and Parameters


#function that greets a user by name
def greet(name): # 'name' is a parameter
    print("Hello,", name, "!")


#in this line, we call the function and pass in an actual name

greet ("Jennifer") # 'Jennifer" is the argument or the value we pass into the function

#---------------------Ouput------------------------#
    #Hello, Jennifer !

#--------------------------------------------------#


#function with two parameters: name and age

def introduce(name, age):  # 'name' and 'age' are parameters
    print(f"My name is {name} and I am {age} years old.")

introduce("Jennifer", 25) 
#---------------------Ouput------------------------#

#Function with return value

def square(number): # 'number' is a parameter
    return number * number # returns the square of the number

result = square(4) #4 is the argument
print ("The square is: " , result) 

#-----------------------------------------------------#

#Function with default parameter value

def greet_user(name = "User"): #'name' has a default value of "User"
    print("Welcome, ", name)

greet_user() #Uses the default argument 
greet_user("Ana") # overrides the default with the argument "Ana"

















