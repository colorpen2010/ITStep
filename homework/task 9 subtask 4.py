numbers = []

n = int(input("Сколько чисел будет в списке: "))

for i in range(n):
    x = int(input("Введите число: "))
    numbers.append(x)

for i in range(n):
    if numbers[i] % 2 == 0:
        print("Индекс парного числа:", i)