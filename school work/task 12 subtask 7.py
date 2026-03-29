try:
    txt = input("Введите числа через пробел: ")

    parts = txt.split()

    nums = []

    for p in parts:

        try:
            nm = float(p)
            nums.append(nm)

        except ValueError:
            print("Предупреждение! Пропущено значение:", p)

    s = sum(nums)
    avg = s / len(nums)

    print("Сумма:", s)
    print("Среднее:", avg)

except ZeroDivisionError:
    print("Нет корректных чисел для вычислений.")

finally:
    print("Обработка данных завершена")