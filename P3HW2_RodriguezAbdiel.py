# Abdiel Rodriguez
# 10 MARCH 2025
# P3HW2
# Determine Employee's Reg Pay and OT Pay and Gross Pay.

#Enter Demographics:
Emp_Name = input("Enter Employee's name: ")
Emp_Hours = int(input("Enter number of hours worked: "))
Pay_Rate = float(input("Enter Employee's pay rate: $"))

print("----------------------------------------")

#calculate some values

if Emp_Hours > 40:
    OT_Hrs = Emp_Hours - 40
    Reg = Pay_Rate * 40

else:
    OT = False
    OT_Hrs = 0
    Reg = Pay_Rate * Emp_Hours

OT = False
OT_Rate= Pay_Rate * 1.5
OT_Pay = OT_Hrs * OT_Rate
Gross = Reg + OT_Pay




print(f"Employee Name: {Emp_Name:<20}")
print()
print(f"{'Hours Worked':<20}{'Pay Rate':<15}{'Overtime':<15}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}") 
print("--------------------------------------------------------------------------------------")
print(f"{Emp_Hours:<20.2f}{Pay_Rate:<15.2f}{OT_Hrs:<15.2f}{OT_Pay:<15.2f}{Reg:<15.2f}{Gross:<15.2f}")