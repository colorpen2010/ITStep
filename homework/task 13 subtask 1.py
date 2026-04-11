import turtle

t = turtle.Turtle()

t.speed(3)

# Квадрат (красный)
t.color('red')

for i in range(4):
    t.forward(100)
    t.right(90)

# Перемещение
t.penup()
t.forward(150)
t.pendown()


# Треугольник (зеленый)
t.color('green')

for i in range(3):
    t.forward(100)
    t.left(120)


# Перемещение
t.penup()
t.forward(150)
t.pendown()


# Пятиугольник (синий)
t.color('blue')

for i in range(5):
    t.forward(100)
    t.right(72)


turtle.done()