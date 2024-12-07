import turtle

# Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
PIPE_TOP_SHAPE = 'pipetop.gif'
PIPE_BOTTOM_SHAPE = 'pipebottom.gif'
PLAYER_SHAPE = 'turtle'
PLAYER_COLOR = 'green'
SCORE_POSITION = (0, 150)
FONT = ("Courier", 24, "normal")
PIPE_SPEED = 4
GO_UP_INCREMENT = 30

class FlappyGame:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.wn.register_shape(PIPE_TOP_SHAPE)
        self.wn.register_shape(PIPE_BOTTOM_SHAPE)

        self.player = turtle.Turtle()
        self.player.shape(PLAYER_SHAPE)
        self.player.color(PLAYER_COLOR)
        self.player.penup()
        self.player.speed(0)
        self.player.goto(0, 0)

        self.score_writer = turtle.Turtle()
        self.score_writer.hideturtle()
        self.score_writer.penup()
        self.score_writer.speed(0)
        self.score_writer.goto(SCORE_POSITION)
        self.score_writer.write("Score: 0", align="center", font=FONT)

        self.game_over_var = False
        self.pipes = []
        self.pipe_speed = PIPE_SPEED
        self.score_var = 0

    def go_up(self):
        y = self.player.ycor()
        y += GO_UP_INCREMENT
        self.player.sety(y)

# Create an instance of the game
game = FlappyGame()

# Example of calling a function
game.go_up()

# Keep the window open
turtle.mainloop()