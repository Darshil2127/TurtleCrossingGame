from turtle import Turtle
START_POSITION = (0,-280)
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.go_to_start()

    def go_up(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(START_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False