number = float(input("Введіть число: "))
power = float(input("Введіть степінь (від 0 до 7): "))

if power < 0 or power > 7:
    print("Помилка: степінь має бути від 0 до 7")
else:
    result = number ** power
    print("Результат:", result)
