<<<<<<< HEAD
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
=======
try:
    prc = float(input("Введите цену товара: "))
    disc = float(input("Введите процент скидки: "))

    final_prc = prc - (prc * disc / 100)

    print("Финальная цена:", final_prc)

except ValueError:
    print("Ошибка ввода! Нужно вводить числа.")
>>>>>>> 2226caf6316ffe7490d1cf1bb04573a39cf9e0ff
