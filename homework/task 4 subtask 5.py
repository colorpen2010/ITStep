a = float(input("введите первое число: "))
b = float(input("введите второе число: "))
op = input("введите операцию: ")  # + - * / % **

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "%":
    print(a % b)
elif op == "**":
    print(a ** b)

