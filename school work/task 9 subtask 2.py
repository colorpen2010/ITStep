nums = list(map(int, input("Введите числа через пробел: ").split()))
x = int(input("Какое число искать: "))

count = nums.count(x)

print("Число:", count)
