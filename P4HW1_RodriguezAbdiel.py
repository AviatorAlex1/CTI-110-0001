# Abdiel Rodriguez 
# 20 MARCH 2025
# P4HW1
# This program takes custom user input scores and provides demographics for it while using loops.


# VARIABLES
num_score = int(input("How many scores do you want to enter? "))
gradeList = []

#Meat and potatoes of the code

for score in range(num_score):
    grade = float(input(f"Enter Score #{score + 1}: "))
    while grade < 0 or grade > 100:
        print("INVALID Score Entered!!!!")
        print("Score should be between 0 and 100")
        grade = float(input(f"Enter score {score + 1} again: ")) 
    gradeList.append(grade)

#performing some "math"

low = min(gradeList)
gradeList.remove(low)
total = sum(gradeList)
avg = total / len(gradeList)

# Display all the results
print()
print("------------Results------------")
print(f"{'Lowest Grade' :<15}{':':<2} {low:.1f}")
print(f"{'Modified List' :<15}{':':<2} {gradeList}")
print(f"{'Scores Average' :<15}{':':<3}{avg:.2f}")

#Printing the letter grade

if avg >= 90:
    print(f"{'Your Grade is' :<15}{':' :<2} A ")
elif avg >= 80:
    print(f"{'Your Grade is' :<15}{':' :<2} B ")
elif avg >= 70:
    print(f"{'Your Grade is' :<15}{':' :<2} C ")
elif avg >= 60:
    print(f"{'Your Grade is' :<15}{':' :<2} D ")   
else:
    print(f"{'Your Grade is' :<15}{':' :<2} F ")

print("-------------------------------")


# PSUEDOCODE REQUIREMENT PER THE INSTRUCTIONS.
'''
create empty list to hold grades
(int)num_scores -> get input from user (how many scores to enter)

FOR LOOP
for "SCORE" in range(num_score):
    get one score from user -> put in a variable as integer
    grade = int(input(f"Enter Score #{score + 1}"))
    WHILE LOOP ---------------------------------------------------------> while "GRADE" is invalid
                                                                          while grade is less than 0 OR grade is greater than 100: 
                                                                          tell the user grade is invalid then allow for user to try again
                                                                          grade = int(input(enter score # {score + 1} again!)
    add grade to list
DONE WITH FOR LOOP

DO MATH!
Get Lowest Number from List
Delete said lowest number from list
Time to do the average... Sum of List divided by total number of numbers in list (LEN)
Display the Lowest Number, Display the MODIFIED LIST and Display the Average
After computing the average display a letter grade to go along with the average. 

as per the instructions... write pseudocode :)
'''