import turtle

t = turtle.Turtle()
t.speed(3)

t.color("red")
t.penup()
t.goto(-200, 0)
t.pendown()

for i in range(4):
    t.forward(100)
    t.right(90)

t.color("green")
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)

t.color("blue")
t.penup()
t.goto(200, 0)
t.pendown()

for i in range(5):
    t.forward(100)
    t.left(72)

turtle.done()