import turtle
import random

# Create a turtle screen
screen = turtle.Screen()
screen.setup(800, 600)

# Create a turtle
t = turtle.Turtle()


turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
t.speed(0)

num=0

for _ in range (100):
    # chose a random color
    color = random_color()
    t.pencolor(color)
    #draw a circle with radius 100
    t.circle(100)
    num+=10
    t.setheading(num)








# Close the turtle graphics window on click
screen.exitonclick()





























