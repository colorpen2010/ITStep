nums = list(map(int, input("Введите числа: ").split()))

s = 0
for n in nums:
    if n > 0:
        s += n

print("Сумма положительных:", s)
