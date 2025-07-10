#Oriana J.

#Day 4: Python Loops


#---------------------------------------------#
#For Loop

print("Counts from 1 to 5 using for loop:")
for i in range(1,6):
    print(i);

#------------------Example output-------------#
    #Counts from 1 to 5 using for loop:
    #1
    #2
    #3
    #4
    #5

#---------------------------------------------#

#While Loop 

print("\n Counting down from 5: ")
count = 5
while count > 0:
    print(count)
    count -= 1
    
#------------------Example output-------------#
    #Counting down from 5: 
    #5
    #4
    #3
    #2
    #1

#---------------------------------------------#

#break
print ("\n Breaking at 3: ")
for i in range(10):
    if i == 3:
        break
    print(i)

#------------------Example output-------------#
    # Breaking at 3: 
    #0
    #1
    #2
#---------------------------------------------#

#continue

print("\n Skipping 3:")
for i in range(5):
    if i == 3:
        continue
    print(i)
    
#------------------Example output-------------#
     #Skipping 3:
    #0
    #1
    #2
    #4

#---------------------------------------------#



