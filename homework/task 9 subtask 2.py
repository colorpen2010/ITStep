numbers = []

n = int(input("Сколько чисел будет в списке: "))

for i in range(n):
    x = int(input("Введите число: "))
    numbers.append(x)

find = int(input("Введите число для поиска: "))

count = 0
for i in range(n):
    if numbers[i] == find:
        count = count + 1

print("Количество:", count)