 # Abdiel Rodriguez
 # 2/12/2025
 # P1HW2    
 # Creating a program that does some basic math on numbers that are entered.

print("This program calculates and displays travel expenses")
print("")

#Establish a budget
budget = int(input("Enter your budget "))

#Enter Travel Destination
destination = input("Enter your Travel Destination ")

#Enter Gas Estimate
fuel = int(input("How much do you think you will spend on gas? "))

#Enter Accomdation Estimate
accomdation = int(input("Approximately, How much will you need for accomodation/hotel? "))

#Enter Food Estimate
food = int(input("Last, how much do you need for food? "))

#Lets throw it all together.
expenses = fuel + accomdation + food
balance = budget - expenses

print("")
print("------------Travel Expenses------------")
print(f"{'Location: ':<20}{destination}")
print(f"{'Initial Budget: ':<20}${budget:.2f}")
print(f"{'Fuel: ':<20}${fuel:.2f}")
print(f"{'Accomdation: ':<20}${accomdation:.2f}")
print(f"{'Food: ':<20}${food:.2f}")
print("---------------------------------------")
print("")
print(f"{'Remaining Balance: ':<20}${balance:.2f}")