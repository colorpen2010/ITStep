import turtle

t = turtle.Turtle()
t.speed(3)

t.color("black")
t.fillcolor("lightblue")

t.begin_fill()
for i in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()

t.left(90)
t.forward(150)
t.right(90)

t.color("red")
t.fillcolor("red")

t.begin_fill()
t.left(45)
t.forward(106)

t.right(90)
t.forward(106)

t.right(135)
t.forward(150)
t.end_fill()

turtle.done()