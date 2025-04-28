# Abdiel Rodriguez
# 26 MARCH 2025
# P4HW2
# Determine multiple Employee's Reg Pay and OT Pay and Gross Pay.
#-------------------------------------------------------

#ACCUMULATOR VARIABLES 
total_Num_Emp = 0
total_OT = 0
total_RegHrs = 0
total_gross = 0

#Initiate Employee Name or Stop Program
Emp_Name = input("Enter Employee Name (or 'Done' once complete): ")

#Start the while loop and have it check to see if the a employee's name has been entered or if the word "Done"/"done" has been entered to bypass adding more employee's to the list.
while Emp_Name.lower() != 'done':
    Emp_Hours = int(input(f"How many hours did {Emp_Name} work?: "))
    Pay_Rate = float(input(f"What is {Emp_Name}'s pay rate?: $"))

    print("----------------------------------------")

    #calculate some values

    if Emp_Hours > 40:
        OT_Hrs = Emp_Hours - 40
        Reg = Pay_Rate * 40

    else:
        OT = False
        OT_Hrs = 0
        Reg = Pay_Rate * Emp_Hours

    #Calculate OT Time and Pay
    OT = False
    OT_Rate= Pay_Rate * 1.5
    OT_Pay = OT_Hrs * OT_Rate
    Gross = Reg + OT_Pay

    #Add to Accummaltor values
    total_Num_Emp += 1
    total_OT += OT_Pay
    total_RegHrs += Reg
    total_gross += Gross

    #Print the Employee Pay data
    print(f"Employee Name: {Emp_Name:<20}")
    print()
    print(f"{'Hours Worked':<20}{'Pay Rate':<15}{'Overtime':<15}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}") 
    print("--------------------------------------------------------------------------------------")
    print(f"{Emp_Hours:<20.2f}{Pay_Rate:<15.2f}{OT_Hrs:<15.2f}{OT_Pay:<15.2f}{Reg:<15.2f}{Gross:<15.2f}")
    print()
    print()

    #Provide the input to Repeat the loop or end the program
    Emp_Name = input("Enter Employee Name (or 'Done' once complete): ")

#Print the Overall Program Data utilizing the values in the accumulator values
print(f"Total Numbers of Employees entered:  {total_Num_Emp}")
print(f"Total amount paid for overtime:  {total_OT:.2f}")
print(f"Total amount paid for Regular Hours:  {total_RegHrs:.2f}")
print(f"Total amount paid in gross:  {total_gross:.2f}")
