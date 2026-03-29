import turtle as t
from turtle_config import *

t.shape(SHAPE)
t.pensize(PEN_SIZE)
# t.color("red")
# t.color("#2eff25")
t.color(COLOR)
t.fillcolor(FILL_COLOR)
t.speed(SPEED)

print_config()

# t.forward(100)
# t.right(80)
# t.forward(40)
# t.left(50)
# t.back(100)

# t.begin_fill()
# t.circle(25)
# t.end_fill()

# t.penup()
# t.goto(-100, 100)
# t.pendown()

# t.circle(150)

screen = t.Screen()

screen.onkey(lambda: t.forward(5), 'w')
screen.onkey(lambda: t.right(15), 'd')
screen.onkey(lambda: t.back(5), 's')
screen.onkey(lambda: t.left(15), 'a')
screen.onclick(lambda x, y: t.goto(x, y))

screen.listen()

t.done()