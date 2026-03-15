import math

try:
    nm = float(input("Введите число: "))

    if nm < 0:
        raise Exception("Нельзя вычислить корень из отрицательного числа")

    res = math.sqrt(nm)

    print("Квадратный корень:", res)

except ValueError:
    print("Ошибка! Нужно ввести число.")

except Exception as err:
    print("Ошибка:", err)

finally:
    print("Вычисления завершены")