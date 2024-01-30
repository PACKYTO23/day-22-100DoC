from turtle import Turtle


class Ball(Turtle):
    """Models the initial ball body."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Generates first ball movement."""
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        """Generates the ball's bounce movement on walls."""
        self.y_move *= -1

    def bounce_x(self):
        """Generates the ball's bounce movement on paddles."""
        self.x_move *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        """Generates restarting ball movement."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
