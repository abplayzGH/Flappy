import turtle
import random


# Set up the screen
wn = turtle.Screen()
wn.title("Flappy")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# Create a turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.goto(0, 0)

def go_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def go_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def generate_pipe():
    pipe = turtle.Turtle()
    pipe.shape("square")
    pipe.color("red")
    pipe.penup()
    pipe.speed(0)
    pipe.goto(400, random.randint(-200, 200))

    return pipe

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")

# Main game loop
while True:
    wn.update()