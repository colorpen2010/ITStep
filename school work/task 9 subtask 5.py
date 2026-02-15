nums = list(map(int, input("Введите числа: ").split()))

unique = []
for n in nums:
    if nums.count(n) == 1:
        unique.append(n)

print("Уникальные элементы:", unique)
