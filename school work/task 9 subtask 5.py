nums = list(map(int, input("Введите числа: ").split()))

unique = []

for n in nums:
    if nums.count(n) == 1:
        # если число встречается 1 раз → уникальное
        unique.append(n)
        # append() — добавить элемент в список

print("Уникальные:", unique)
