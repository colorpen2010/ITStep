n = int(input("Введите количество чисел: "))

max_num = int(input("Введите число: "))

for i in range(n - 1):
    x = int(input("Введите число: "))
    if x > max_num:
        max_num = x

print("Самое большое число:", max_num)
