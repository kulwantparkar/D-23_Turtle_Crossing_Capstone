from turtle import Turtle
STARTING_POSITION = (0, -220)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 240


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_again()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def start_again(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

