text = input("Введите ряд: ")

words = text.split()
longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print("Самое длинное слово:", longest)
