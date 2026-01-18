number = int(input("Введіть чотиризначне число: "))

a = number // 1000
b = number // 100 % 10
c = number // 10 % 10
d = number % 10

summa = a + b + c + d

if summa % 2 == 0:
    print("Сума цифр парна")
else:
    print("Сума цифр непарна")
