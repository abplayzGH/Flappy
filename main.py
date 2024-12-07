import turtle
import random


# Set up the screen
wn = turtle.Screen()
wn.title("Flappy")
wn.bgcolor("lightblue")
wn.setup(width=500, height=400)
wn.register_shape('pipetop.gif')
wn.register_shape('pipebottom.gif')

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
score_writer.write("Score: 0", align="center", font=("Courier", 24, "normal"))

#variables

game_over_var = False
pipes = []
pipe_speed = 2
score_var = 0
# Functions

def go_up():
    y = player.ycor()
    y += 30
    player.sety(y)

def gravity():
    y = player.ycor()
    y -= 2
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
    pipe.goto(300, random.randint(100, 200))
    pipe.setheading(180)
    pipe.showturtle()
    return pipe

def generate_pipe_bottom():
    pipe = turtle.Turtle()
    pipe.hideturtle()
    pipe.shape("pipebottom.gif")
    pipe.penup()
    pipe.speed(0)
    pipe.goto(300, random.randint(-200, -100))
    pipe.setheading(180)
    pipe.showturtle()
    return pipe

def create_pipes():
    pipes.append(generate_pipe_top())
    pipes.append(generate_pipe_bottom())
    
def move_pipe():
    global game_over_var
    if game_over_var:
        return None
    else:
        if pipes[0].xcor() < -300:
            for i in range (len(pipes)):
                pipes[i].clear()
                pipes[i].hideturtle()
            pipes.clear()
            create_pipes()
        else:
            for item in range (len(pipes)):
                pipes[item].forward(pipe_speed)

#Collision Detection

def collision_detection():
    for item in range (len(pipes)):
        if player.distance(pipes[item]) < 40:
            game_over()

#score functions

def score():
    global score_var
    if player.xcor() == pipes[0].xcor():
        score_var += 1
        print(score_var)
        score_writer.clear()
        score_writer.write((f"Score: {score_var}"), align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(gravity, "Down")

# Main game loop
create_pipes()
while True:
    collision_detection()
    gravity()
    move_pipe()
    score()
    wn.update()