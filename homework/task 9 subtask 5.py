numbers = []

n = int(input("Сколько чисел будет в списке: "))

for i in range(n):
    x = int(input("Введите число: "))
    numbers.append(x)

unique = []

for i in range(n):
    count = 0
    for j in range(n):
        if numbers[i] == numbers[j]:
            count = count + 1

    if count == 1:
        unique.append(numbers[i])

print("Уникальные числа:", unique)