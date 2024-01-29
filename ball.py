from turtle import Turtle

POSITION = (0, 0)


class Ball(Turtle):
    """Models the initial ball body."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.move()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Generates first ball movement."""
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce(self):
        """Generates the ball's bounce movement."""
        self.y_move *= -1
