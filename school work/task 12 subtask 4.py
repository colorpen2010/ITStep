<<<<<<< HEAD
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
=======
try:
    txt = input("Введите оценки через пробел: ")

    parts = txt.split()

    nums = []

    for p in parts:
        nums.append(int(p))

    s = sum(nums)
    avg = s / len(nums)

    print("Средняя оценка:", avg)

except ValueError:
    print("Ошибка! Оценки должны быть числами.")

except ZeroDivisionError:
    print("Список оценок пуст.")

finally:
    print("Завершение вычислений")
>>>>>>> 2226caf6316ffe7490d1cf1bb04573a39cf9e0ff
