#Oriana J.
#Day 7 Practice


#Task 1: Create a Function with Parameters and Arguments
#Write a function called greet_user that:
#Takes in 2 parameters: name (a string) and language (a string).
#If the language is "english", print "Hello, [name]!"
#If the language is "spanish", print "¡Hola, [name]!"
#Otherwise, print "Hi, [name]! (language not recognized)"
#Call the function 3 times using different arguments.

def greet_user(name, language):
    if language == "english":
        print(f"Hello, {name}!")
    elif language == "spanish":
        print (f"¡Hola, {name}!")
    else:
        print (f"Hi, {name}! (language not recognized)")

greet_user("Jenni", "english")   #Hello, Jenni!
greet_user("Lucia","spanish")   #¡Hola, Lucia!
greet_user("Jordan", "french")  #(language not recognized)
