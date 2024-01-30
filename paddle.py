from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90


class Paddle(Turtle):
    """Models the initial paddle body."""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(UP)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def up(self):
        """Moves paddle up."""
        self.forward(MOVE_DISTANCE)

    def down(self):
        """Moves paddle down."""
        self.forward(-MOVE_DISTANCE)
