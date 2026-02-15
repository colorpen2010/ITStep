nums_str = input("Введите числа: ").split()

nums = []
for n in nums_str:
    nums.append(int(n))

s = 0

for n in nums:
    if n > 0:
        s += n

print("Сумма положительных:", s)