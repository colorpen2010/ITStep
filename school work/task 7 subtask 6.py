height = int(input("Введите висоту триугольника: "))
symbol = input("Введите символ: ")

for i in range(1, height + 1):
    spaces = height - i
    symbols = 2 * i - 1
    print(" " * spaces + symbol * symbols)
