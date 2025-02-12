#This program calculates energy in Joules
 
print("Calculate energy based on mass entered!!")

# Get the Mass from the user
mass = float(input("Enter the Mass of the Object: ")) 

#Delare the Speed of light: 299 792 458 m / s (x2: 599 584 916)

speed_of_light = 299792458

#Solve for E

energy = mass * speed_of_light ** 2 

print("The Formula for energy is: mass * speed_of_light ** 2 and the value is", energy)
