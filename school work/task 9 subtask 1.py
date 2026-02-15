nums = list(map(int, input("Введите числа через пробел: ").split()))

s = sum(nums)
avg = s / len(nums)

print("сумма:", s)
print("Среднее:", avg)
