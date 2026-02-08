txt = input("Введите ряд: ")

latters = 0
cifr = 0

for ch in txt:
    if ch.isalpha():
        latters += 1
    elif ch.isdigit():
        cifr += 1

print("Букв: ", latters)
print("Цифр: ", cifr)
