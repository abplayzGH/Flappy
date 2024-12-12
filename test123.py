import turtle
import random
import time
import gc


# Set up the screen
wn = turtle.Screen()
wn.title("Flappy")
wn.bgcolor("lightblue")
wn.setup(width=500, height=400)
wn.register_shape('pipetop.gif')
wn.register_shape('pipebottom.gif')
wn.tracer(0)

# Create a turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.goto(0, 0)

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.speed(0)
score_writer.goto(0, 150)
score_writer.pendown()
score_writer.write("Score: 0", align="center", font=("Courier", 24, "normal"))

#variables

game_over_var = False
pipes = []
pipe_speed = 4
score_var = 0

# Functions

def go_up():
    y = player.ycor()
    y += 75
    player.sety(y)

def gravity():
    y = player.ycor()
    y -= 5
    player.sety(y)
    if player.ycor() <= -200 or player.ycor() >= 200:
        game_over()

def game_over():
    global game_over_var
    player.hideturtle()
    player.goto(0, 0)
    player.write("Game Over", align="center", font=("Courier", 24, "normal"))
    game_over_var = True
    
#pipe functions   
def generate_pipe_top():
    pipe = turtle.Turtle()
    pipe.hideturtle()
    pipe.shape("pipetop.gif")
    pipe.penup()
    pipe.speed(0)
    pipe.goto(300, random.randint(125, 200))
    pipe.setheading(180)
    pipe.showturtle()
    return pipe

def generate_pipe_bottom():
    pipe = turtle.Turtle()
    pipe.hideturtle()
    pipe.shape("pipebottom.gif")
    pipe.penup()
    pipe.speed(0)
    pipe.goto(300, random.randint(-200, -125))
    pipe.setheading(180)
    pipe.showturtle()
    return pipe

def create_pipes():
    pipes.extend([generate_pipe_top(), generate_pipe_bottom()])
    
def move_pipe():
    for pipe in pipes:
        pipe.forward(pipe_speed)
    if pipes[0].xcor() < -300:
        for pipe in pipes:
            pipe.hideturtle()
        pipes.clear()
        create_pipes()


#Collision Detection

def collision_detection():
    for item in range (len(pipes)):
        if player.distance(pipes[item]) < 75:
            game_over()

#score functions

def score():
    global score_var
    if player.xcor() == pipes[0].xcor():
        score_var += 1
        score_writer.clear()
        score_writer.write((f"Score: {score_var}"), align="center", font=("Courier", 24, "normal"))
        if score_var % 5 == 0:
            global pipe_speed
            pipe_speed += 1


# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")


#create pipes
create_pipes()
time.sleep(2)
    
while not game_over_var:
    gc.collect()
    collision_detection()
    gravity()
    move_pipe()
    score()
    wn.update()
    time.sleep(0.02)
    wn.update()