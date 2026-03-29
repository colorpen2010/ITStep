try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    res = a / b

    print("Результат деления:", res)

except ValueError:
    print("Ошибка! Нужно вводить числа.")

except ZeroDivisionError:
    print("Ошибка! Деление на ноль.")

finally:
    print("Операция завершена")