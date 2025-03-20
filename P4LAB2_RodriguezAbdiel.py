# Abdiel Rodriguez
# 19 MARCH 2025
# P4LAB2
# create a program that utilizes loops and will multiply the user given input


run_again = "yes"

while run_again != "no":
    user_num = int(input("Enter an Integer: "))

    if user_num < 0:
        print("This program do not support negative numbers")

    else:
        for i in range(1,13):
            print(f"{user_num} * {i} = {user_num * i}")
            
    run_again = input(print("Would you like to run the program again? (yes/no)"))
print("Program has ended.........")