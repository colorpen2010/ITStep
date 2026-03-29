<<<<<<< HEAD
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
=======
try:
    usd = float(input("Введите сумму в долларах: "))
    rate = float(input("Введите курс евро: "))

    if rate == 0:
        raise Exception("Курс обмена не может быть нулем")

    eur = usd / rate

    print("Сумма в евро:", eur)

except ValueError:
    print("Ошибка ввода! Нужно вводить числа.")

except Exception as e:
    print("Ошибка:", e)

finally:
    print("Операция завершена")
>>>>>>> 2226caf6316ffe7490d1cf1bb04573a39cf9e0ff
