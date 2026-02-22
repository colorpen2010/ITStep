numbers = []

n = int(input("Сколько чисел будет в списке: "))

for i in range(n):
    x = int(input("Введите число: "))
    numbers.append(x)

s = 0
for i in range(n):
    if numbers[i] > 0:
        s = s + numbers[i]

print("Сумма положительных чисел:", s)