nums_str = input("Введите числа: ").split()

nums = []
for n in nums_str:
    nums.append(int(n))

x = int(input("Какое число искать: "))

count = nums.count(x)

print("Количество:", count)