nums = list(map(int, input("Введите числа: ").split()))

s = 0

for n in nums:       # for — перебирает элементы списка по одному
    if n > 0:        
        s += n       

print("Сумма положительных:", s)
