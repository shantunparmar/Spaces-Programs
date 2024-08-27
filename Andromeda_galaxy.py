import turtle
import time
import random

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")

# Create a new turtle object for the stars
stars = []
for _ in range(100):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("white")
    star.speed(0)
    star.penup()
    star.goto(random.randint(-300, 300), random.randint(-300, 300))
    star.pendown()
    stars.append(star)

# Create a new turtle object for the planets
planets = []
for _ in range(10):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color("blue")
    planet.speed(0)
    planet.penup()
    planet.goto(random.randint(-200, 200), random.randint(-200, 200))
    planet.pendown()
    planets.append(planet)

# Create a new turtle object for the black hole
black_hole = turtle.Turtle()
black_hole.shape("circle")
black_hole.color("red")
black_hole.speed(0)
black_hole.penup()
black_hole.goto(0, 0)
black_hole.pendown()

# Function to move the stars
def move_stars():
    for star in stars:
        star.forward(1)
        if star.xcor() > 300 or star.xcor() < -300 or star.ycor() > 300 or star.ycor() < -300:
            star.goto(random.randint(-300, 300), random.randint(-300, 300))

# Function to move the planets
def move_planets():
    for planet in planets:
        planet.forward(1)
        if planet.xcor() > 200 or planet.xcor() < -200 or planet.ycor() > 200 or planet.ycor() < -200:
            planet.goto(random.randint(-200, 200), random.randint(-200, 200))

# Function to move the black hole
def move_black_hole():
    black_hole.right(1)

# Animate the Andromeda galaxy
while True:
    move_stars()
    move_planets()
    move_black_hole()
    time.sleep(0.01)
