text = input("Введите текст: ")
bad = input("Введите символы: ")

words = text.split()
result = ""

for w in words:
    ok = True

    for ch in bad:
        for letter in w:
            if letter == ch:
                ok = False

    if ok:
        result += w + " "

print(result)
