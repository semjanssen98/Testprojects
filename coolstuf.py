import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    turtle.color(c)
    turtle.left(10)
    turtle.fd(2)
    for j in range(2):
        turtle.left(2)
        turtle.circle(10)
