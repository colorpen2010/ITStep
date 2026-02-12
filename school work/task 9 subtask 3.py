reserved = ["if", "for", "while", "print"]

text = input("Введите текст: ")
words = text.split()

result = ""

for w in words:
    if w in reserved:
        result += w.upper() + " "
    else:
        result += w + " "

print(result)
