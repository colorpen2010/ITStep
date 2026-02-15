nums = list(map(int, input("Введите числа: ").split()))

x = int(input("Какое число искать: "))
count = nums.count(x)
# count() — считает сколько раз число есть в списке

print("Количество:", count)
