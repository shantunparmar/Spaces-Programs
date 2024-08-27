import turtle
import time

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")

# Create a new turtle object for the Earth
earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.speed(0)

# Create a new turtle object for the Moon
moon = turtle.Turtle()
moon.shape("circle")
moon.color("gray")
moon.speed(0)

# Function to rotate the Earth
def rotate_earth():
    earth.right(1)

# Function to rotate the Moon
def rotate_moon():
    moon.right(3)

# Function to move the Moon around the Earth
def orbit_moon():
    moon.forward(1)
    moon.right(0.5)

# Draw the Earth
earth.penup()
earth.goto(0, 0)
earth.pendown()
earth.begin_fill()
earth.circle(50)
earth.end_fill()

# Draw the Moon
moon.penup()
moon.goto(100, 0)
moon.pendown()
moon.begin_fill()
moon.circle(10)
moon.end_fill()

# Animate the rotation of the Earth and the Moon
while True:
    rotate_earth()
    rotate_moon()
    orbit_moon()
    time.sleep(0.01)
