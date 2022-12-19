import random
import turtle


class food:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('circle')
        self.t.shapesize(0.5)
        self.t.color('white')
        self.t.penup()
        self.new_food()

    def new_food(self):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        self.t.hideturtle()
        self.t.setposition(x * 20, y * 20)
        self.t.showturtle()
