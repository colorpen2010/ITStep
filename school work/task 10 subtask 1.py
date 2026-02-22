numbers = input("Введите числа через пробел: ").split()

nums = []
for i in range(len(numbers)):
    nums.append(int(numbers[i]))

unique_nums = set(nums)

print("Уникальные элементы:", unique_nums)