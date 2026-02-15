nums_str = input("Введите числа: ").split()

nums = []
for n in nums_str:
    nums.append(int(n))

unique = []

for n in nums:
    if nums.count(n) == 1:
        unique.append(n)

print("Уникальные:", unique)