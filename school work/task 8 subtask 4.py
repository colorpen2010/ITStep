text = input("Введите ряд: ")
word = input("Введите слово: ")

words = text.split()
count = 0

for w in words:
    if w == word:
        count += 1

print("Число: ", count)
