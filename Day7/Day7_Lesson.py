#Oriana J.

#Day 7 Default Parameters, Return, Print, and Docstrings


#function with a default parameter
def welcome_message(user = "Guest"): # 'user is a parameter default value is 'guest'
    return f"welcome, {user}!"
    
def show_difference(x, y): #x and y are parameters
    return x - y #returns the result (argument is used when function is called)

def print_difference(x,y):
    print(x - y) #only prints result 

# Function with a docstring
def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    
    Parameters:
    a (int or float): The first number
    b (int or float): The second number
    
    Returns:
    int or float: The product of a and b
    """
    return a * b





# Testing the functions
print(welcome_message()) # Uses default argument 'Guest'
print(welcome_message("Jenni")) # Passes "Jenni" as argument

result = show_difference(10, 3)
print("Returned value:", result)

print("Printed value:")
print_difference(5, 3)

# Using multiply function
print("Multiplication:", multiply(5, 4))
