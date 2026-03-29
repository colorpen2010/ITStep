def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

res = gcd(a, b)

print("НОД чисел:", res)