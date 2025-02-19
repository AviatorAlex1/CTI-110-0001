# Abdiel
# Rodriguez
# P2LAB2
# Writing code that uses a dictionary to store user input and displays output to the user

#-----------------------------------------------------------------------------------------------

#Starting the Dictionary for the Vehicle MPG
Veh_MPG = {"Camaro" : 18.21, "Prius" : 52.36, "Model S" : 110, "Silverado" : 26}

# Recalling the MPGs from the Dictionary with a variable
keys = Veh_MPG.keys()

# Display the Keys from Dictionary above
print(keys)

# User Input requesting a specific key
Vehicle = input("Enter A vehicle to see its MPG: ")

#State the selected vehicle's MPG
print(f" The {Vehicle} gets {Veh_MPG[Vehicle]} MPG. ")

# User input stating the miles to be driven 
miles = float(input(f"How many miles will you drive the {Vehicle}? "))

# Doing some math for the MPG Calculations
math = miles / Veh_MPG[Vehicle]

# Display the Total gallons of gas to drive the given number of miles
print(f"{math:.2f} gallon(s) of gas are needed to drive the {Vehicle} {miles} miles.")