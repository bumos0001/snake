import turtle


class score:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.penup()
        self.score = 0
        self.t.setposition(-50, 350)
        self.t.write(f"Score: {self.score}", font=('Arial', 20, 'normal'))
        self.t.pencolor('white')
        self.t.hideturtle()

    def add_score(self):
        self.score += 1
        self.t.clear()
        self.t.pencolor('white')
        self.t.write(f"Score: {self.score}", font=('Arial', 20, 'normal'))