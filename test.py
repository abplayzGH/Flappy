import turtle
import random
import time
import gc
import leaderboard


# Set up the screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.setup(width=500, height=400)
wn.register_shape('pipetop.gif')
wn.register_shape('pipebottom.gif')
wn.register_shape('bird.gif')
wn.tracer(0)

# Create a turtle
player = turtle.Turtle()
player.shape("bird.gif")
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

#leaderboard
leaderboard.add_score("cool", 21)
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
    # leaderboard.add_score("test", score_var)
    
#pipe functions   
def generate_pipe_top():
    pipe = turtle.Turtle()
    pipe.hideturtle()
    pipe.shape("pipetop.gif")
    pipe.penup()
    pipe.speed(0)
    pipe.goto(300, random.randint(150, 200))
    pipe.setheading(180)
    pipe.showturtle()
    return pipe

def generate_pipe_bottom():
    pipe = turtle.Turtle()
    pipe.hideturtle()
    pipe.shape("pipebottom.gif")
    pipe.penup()
    pipe.speed(0)
    pipe.goto(300, random.randint(-200, -150))
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
        if player.distance(pipes[item]) < 80:
            game_over()

#score functions

def update_score():
    global score_var
    global pipe_speed
    for pipe in pipes:
        if player.xcor() > pipe.xcor() and not hasattr(pipe, 'scored'):
            score_var += 0.5
            pipe.scored = True
            score_writer.clear()
            score_writer.write(f"Score: {round(score_var)}", align="center", font=("Courier", 24, "normal"))
            pipe_speed += 0.2

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
    update_score()
    wn.update()
    time.sleep(0.02)
    wn.update()