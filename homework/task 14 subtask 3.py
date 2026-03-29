try:
    txt = input("Введите продажи через пробел: ")

    parts = txt.split()

    nums = []

    for p in parts:
        nums.append(float(p))

    total = sum(nums)

    print("Общая сумма продаж:", total)

except ValueError:
    print("Ошибка! Введите только числа.")

finally:
    print("Обработка завершена")