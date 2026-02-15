nums_str = input("Введите числа через пробел: ").split()

nums = []
for n in nums_str:
    nums.append(int(n))

s = sum(nums)
avg = s / len(nums)

print("Сума:", s)
print("Средние:", avg)