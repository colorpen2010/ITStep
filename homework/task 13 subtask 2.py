import turtle

t = turtle.Turtle()

t.speed(3)

t.color('black')
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.color('red')

t.begin_fill()

t.left(60)
t.forward(100)

t.right(120)
t.forward(100)

t.right(120)
t.forward(100)

t.end_fill()

turtle.done()