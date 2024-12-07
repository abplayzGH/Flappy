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

def go_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def go_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

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

pipes = []
pipe_speed = 2

def create_pipes():
    pipes.append(generate_pipe_top())
    pipes.append(generate_pipe_bottom())
    
def move_pipe():
    if pipes[0].xcor() < -300:
        for i in range (len(pipes)):
            pipes[i].clear()
            pipes[i].hideturtle()
        pipes.clear()
        create_pipes()
    else:
        for item in range (len(pipes)):
            pipes[item].forward(pipe_speed)


# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")

# Main game loop
create_pipes()
while True:
    move_pipe()
    wn.update()