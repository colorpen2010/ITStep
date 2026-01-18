number = input("Введіть шестизначне число: ")

if len(number) != 6:
    print("Помилка: число не шестизначне")
else:
    result = (
        number[5] +
        number[4] +
        number[2] +
        number[3] +
        number[1] +
        number[0]
    )
    print("Результат:", result)
