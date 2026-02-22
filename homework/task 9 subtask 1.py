numbers = []

n = int(input("Сколько чисел будет в списке: "))

for i in range(n):
    x = int(input("Введите число: "))
    numbers.append(x)

s = 0
for i in range(n):
    s = s + numbers[i]

average = s / n

print("Сумма:", s)
print("Среднее:", average)