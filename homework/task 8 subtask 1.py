text = input("Введите текст: ")

count = 0

for c in text:
    if c == "." or c == "!" or c == "?":
        count += 1

print("Количество предложений:", count)
