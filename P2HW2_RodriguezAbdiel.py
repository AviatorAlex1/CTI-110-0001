#Abdiel Rodriguez

 #24 FEB 2025

 #P2HW2

 #Create a code that lets user enter grades and store them in a list being able to displate and provide basic arithmetic functions.

#Entering Grades for assignments
M1_Grade = float(input("Enter Grade for Module 1: "))
M2_Grade = float(input("Enter Grade for Module 2: "))
M3_Grade = float(input("Enter Grade for Module 3: "))
M4_Grade = float(input("Enter Grade for Module 4: "))
M5_Grade = float(input("Enter Grade for Module 5: "))
M6_Grade = float(input("Enter Grade for Module 6: "))

GradeList = [M1_Grade,M2_Grade,M3_Grade,M4_Grade,M5_Grade,M6_Grade]
print()
#Create an empty list 

#use Append method to add all grades into the list
#Code looks like this: list_name.append(what_to_add_to_list)

#Display Results
print("------------Results------------")

print()
#print(GradeList)
#print()
avg = sum(GradeList) / len(GradeList)

print(f"{'Lowest Grade: ':<20} {min(GradeList):.2f}")
print(f"{'Highest Grade: ':<20} {max(GradeList):.2f}")
print(f"{'Sum of Grades:' :<20} {sum(GradeList):.2f}")
print(f"{'Average: ':<20} {avg:.2f}")

print()
print("-------------------------------")