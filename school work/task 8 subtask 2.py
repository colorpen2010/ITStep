text = input("Введите ряд: ")
symbol = input("Введите символ: ")

count = 0

for ch in text:
    if ch == symbol:
        count += 1

print("Число: ", count)
