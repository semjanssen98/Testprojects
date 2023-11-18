####################
# Fibonacci spiral #
# Turtle version   #
####################

import math
import turtle

window = turtle.Screen()
window.setup(1000, 800)
myTurtle = turtle.Turtle()  # set turtle to x=0 and y=0 on screen
myTurtle.pensize(2)


# the function to calculate the value of fib and send the result to the draw function
def main():
    valueOne = 0
    valueTwo = 1
    fib = 1
    for i in range(8):  # number of squares to draw
        myTurtle.right(90)  # point turtle to down position
        drawsq(fib*20)  # call drawSquare function- argument = length of sides
        fib = valueOne + valueTwo  # calculate the fibonacci sequence
        valueOne = valueTwo
        valueTwo = fib



# the function to draw the fibonacci square
def drawsq(sides):
    for n in range(6):  # the value 6 ensures that the start of the next square is correct
        myTurtle.forward(sides)  # draw the sides of the squares
        myTurtle.left(90)  # turn the pointer left 90 degrees


def spiral():
    r = 20
    angle = 90
    myTurtle.right(90)
    myTurtle.penup()
    myTurtle.setpos(0, 0)
    myTurtle.pendown()
    # draw fibonacci spiral || HARDCODED > DYNAMIC
    arc(20, angle)
    arc(20, angle)
    arc(40, angle)
    arc(60, angle)
    arc(100, angle)
    arc(160, angle)
    arc(260, angle)
    arc(420, angle)


def arcline(n, length, angle):
    for i in range(n):
        myTurtle.forward(length)
        myTurtle.left(angle)


# draws an arc with the given radius and angle
def arc(r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    # before starting making a slight left turn
    myTurtle.left(step_angle / 2)
    arcline(n, step_length, step_angle)
    myTurtle.right(step_angle / 2)


main()  # calls the main function wich draws the boxes
spiral()  # calls the spiral function wich draws the spiral
window.exitonclick()  # click on the screen to exit the program
