#Oriana J.

#Day 4 Tasks

#1. 
    #multiples of 3
    #Print all numbers from 1 to 30 that are
    #divisible by 3 using a for loop.
#2
    #Guess the Number Game
    #Pick a secret number between 1 and 10 (use secret = 7)
    #Ask the user to guess using a while loop.
    #Keep asking until they guess right.
    #If wrong, say "Try again!"
#3
    #count total characters
    #Ask the user for a word.
    #Use a for loop to count how many characters it has(without using len())

#------------------------------------------------------------------------#
#1. multiples of 3

for i in range(1,31):
    if i % 3 == 0:
        print(i)
#------------------------Expected output---------------------------------#
    #3
    #6
    #9
    #12
    #15
    #18
    #21
    #24
    #27
    #30
        
#------------------------------------------------------------------------#
#2. Guess the number game
secret = 7
number = int(input("Pick a secret number between 1 and 10: "))

while number != secret:
    print("Wrong! Try again!")
    number = int(input("Pick a secret number between 1 and 10: "))
print ("You got it right!! ")

#------------------------Expected output---------------------------------#
    #Pick a secret number between 1 and 10: 9
    #Wrong! Try again!
    #Pick a secret number between 1 and 10: 4
    #Wrong! Try again!
    #Pick a secret number between 1 and 10: 5
    #Wrong! Try again!
    #Pick a secret number between 1 and 10: 6
    #Wrong! Try again!
    #Pick a secret number between 1 and 10: 7
    #You got it right!! 
#-------------------------------------------------------------------------#

#3. Count total characters

word = input("Enter a word: ")
count = 0

for char in word:
    count += 1

print("The word has", count, "characters.")

#------------------------Expected output---------------------------------#
#Enter a word: Practice
#The word has 8 characters.
       

















