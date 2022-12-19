import turtle
import score
import food
import time
screen = turtle.Screen()
turtle.tracer(9)
screen.listen()
screen.bgcolor("black")


def top():
    if t[0].heading() != 270:
        t[0].setheading(90)


def down():
    if t[0].heading() != 90:
        t[0].setheading(270)


def right():
    if t[0].heading() != 180:
        t[0].setheading(0)


def left():
    if t[0].heading() != 0:
        t[0].setheading(180)


def is_collision():
    if f.t.distance(t[0]) <= 19:
        print("collision")
        f.new_food()
        s.add_score()
        add_length()
        turtle.update()


def add_length():
    a = turtle.Turtle()
    a.shape('square')
    a.shapesize(1)
    a.color('white')
    a.penup()
    a.setposition(t[-1].pos())
    t.append(a)


def self_collision():
    for _ in range(1, len(t)):
        if t[0].distance(t[_]) <= 10:
            return True
    if t[0].xcor() >= 450 or t[0].ycor() >= 450:
        return True


s = score.score()
t = []
for i in range(3):
    t.append(turtle.Turtle())
    t[i].shape('square')
    t[i].shapesize(1)
    t[i].color('white')
    t[i].penup()
    t[i].setposition(20*(-i), 0)

f = food.food()


game_on = True
while game_on:
    for i in range(len(t)-1, 0, -1):
        t[i].goto(t[i-1].xcor(), t[i-1].ycor())
    t[0].forward(20)
    if self_collision():
        print("lose")
        game_on = False

    screen.onkey(top, 'Up')
    screen.onkey(left, 'Left')
    screen.onkey(right, 'Right')
    screen.onkey(down, 'Down')
    is_collision()
    time.sleep(0.1)
    turtle.update()

screen.exitonclick()
