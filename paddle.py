from turtle import Turtle, Screen


class Paddle:
    def __init__(self):
        self.paddle = Turtle()

    def make_paddle(self):
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(-350, 0)