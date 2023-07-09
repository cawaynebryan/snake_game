from turtle import Turtle
from random import randint


class Portal(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.shapesize()
        self.penup()
        self.set_position()

    def set_position(self):
        x_position = randint(0, 250)
        y_position = randint(0, 250)
        self.goto(x_position, y_position)
