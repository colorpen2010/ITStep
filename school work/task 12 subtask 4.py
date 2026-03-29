import turtle
import random

t = turtle.Turtle()
t.speed(0)

colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink"]

for i in range(36):
    t.color(random.choice(colors))

    for j in range(4):
        t.forward(100)
        t.right(90)

    t.right(10)

turtle.done()