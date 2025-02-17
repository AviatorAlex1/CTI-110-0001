#In-Class practice Module 4- Formatting Output

# Get an amount of money from the user
item = input("What Item are you purchasing? ")
money = float(input("Enter Money Amount with Change: "))

#### The plus sign is concatination of strings, not addition
print("The Amount entered: $:"+ str(money))
print()

#Use a formatted String to print a specific amout of placeholders
print(f"The Amount entered is: ${money:.2f} and the item is {item.upper()}")
print()

#This is the Formatted string
print(f"I am buying a {item} and it costs ${money:.2f}")
print()

# This is the unformatted string 
print("I am buying a",item,"and it costs $" + str(money))
print()