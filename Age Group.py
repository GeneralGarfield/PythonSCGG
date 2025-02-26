# Program Age Classifier
# Description: Determines the age and organizes it.
#   
#
# Author: <> 
# Date: <19/2/2025>
# Revised: 
#   <19/2/2025>


#Prints opening Statement

print("Organizes the age and places it in categories. By Ricardo Montoya-Adame")

# This Determines the age and organizes based on the age group
def persons_age():
    person = int(input("What is the age of the person?: "))
    if person <= 1:
        print("they are an infant")
    elif person in range(2,14):
        print("they are a child")
    elif person in range(14,20):
        print("they are a teenager")
    elif person in range(20,61):
        print("They are an adult")
    elif person in range(61,110):
        print("You are a senior")
    elif person > 111:
        print("You're really old. Congrats.")

# Runs the Program
persons_age()

#End of Program
