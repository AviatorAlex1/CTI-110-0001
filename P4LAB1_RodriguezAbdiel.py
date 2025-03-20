# Abdiel Rodriguez
# P4LAB1
# 17 MARCH 2025
# This Program creates turtles graphics to draw a square and triangle with looping

import turtle
win = turtle.Screen()
timmy = turtle.Turtle()

# Options for Timmy
timmy.pensize(2)
timmy.pencolor("red") 
timmy.shape("turtle")

# Start the square drawing
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

#while this loop that runs 3 times

this_run = 0 

while this_run < 3:
    timmy.forward(100)
    timmy.left(120)
    this_run += 1

# Keeping the window open after shape is drawn, user manually closes.
win.mainloop()
