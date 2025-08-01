# Oriana J.

#Day 3 tasks

#Ask the user for their age and respond based on the following rules:
# If under 13: print "You're a kid!"
# If 13 to 19: print "You're a teenager."
# If 20 to 64: print "You're an adult."
# If 65 or older: print "You're a senior."

#BONUS TASK: After the message, print how many years they
#   have until they turn 100.
#Example: "You’re a teenager. You’ll turn 100 in 85 years!"

#Bonus: Add a check to make sure age
#   is between 0 and 100. If it’s not, print “Invalid age!”
#--------------------------------------------------#

age = int(input("Enter your age(0-100): "))

if age < 13:
    print("You're a kid!", "You'll turn 100 in ", 100 - age, "years!")
elif age >= 13 and age <= 19:
    print("You're a teenager.","You'll turn 100 in ", 100 - age, "years!")
elif age >= 20 and age <= 64:
    print("You're an adult.", "You'll turn 100 in ", 100 - age, "years!")
elif age > 64 and age <= 100:
    print("You're a senior.", "You'll turn 100 in ", 100 - age, "years!")
else:
    print("Invalid age!")

#---------------Expected Output--------------------#

#Enter your age(0-100): 95
#You're a senior. You'll turn 100 in  5 years!
