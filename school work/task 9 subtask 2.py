text = input("Введите рядок: ")

rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("Палиндром")
else:
    print("Не палиндром")
