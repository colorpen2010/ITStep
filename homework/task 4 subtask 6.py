num = int(input("введите тризначное число: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a == b and b == c:
    print("Все цыфры одинаковые")
else:
    print("Все цыфры разные")
