#   Abdiel Rodriguez
#   3 March 2025
#   P3lab
#   

OG_money = float(input("Enter the amount of money as a float: $"))

money = int(OG_money * 100)

#Calculate Number of whole Dollars
num_dollars = money // 100

#Remove the Dollar amount from the amount of money
money = money - (num_dollars * 100)

#Calculate Number of Quarters
num_quarters =  money // 25
money = money - (num_quarters * 25)

#Calculate Number of Dimes
num_dimes = money // 10
money = money - (num_dimes * 10)

#Calculate Number of Nickles
num_nickles =  money // 5
money = money - (num_nickles * 5)

#Calculate Number of Pennies
num_pennies =  money

#Display Original Amount
print(f"${OG_money}")
print()

#Display coins/dollars needed only if gthey are used. While Ensuring that Grammar is correct.
# 

#Display Number of Dollars (if Any.)
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar ")
    else:
        print(f"{num_dollars} Dollars ")

#Display Number of Quarters (if Any.)
if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter ")
    else:
        print(f"{num_quarters} Quarters ")

#Display Number of Dimes (if Any.)
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime ")
    else:
        print(f"{num_dimes} Dimes ")

#Display Number of Nickles (if Any.)
if num_nickles > 0:
    if num_nickles == 1:
        print(f"{num_nickles} Nickle ")
    else:
        print(f"{num_nickles} Nickles ")

#Display Number of Pennies (if Any.)
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny ")
    else:
        print(f"{num_pennies} Pennies ")

else:
    print("No Change.")