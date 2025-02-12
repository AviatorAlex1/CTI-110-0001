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
print("Location: ",destination)
print("Initial Budget: ",budget)
print("")
print("Fuel: ",fuel)
print("Accomdation: ",accomdation)
print("Food: ",food)
print("")
print("Remaining Balance: ",balance)