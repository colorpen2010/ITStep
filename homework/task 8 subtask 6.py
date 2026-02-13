text = input("Введите текст: ")

words = text.split()
result = ""

for i in range(len(words) - 1, -1, -1):
    result += words[i] + " "

print(result)
