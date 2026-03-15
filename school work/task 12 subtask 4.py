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