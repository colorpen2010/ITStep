text = input("Введите текст: ")

text = text.lower()

words = text.split()

count_words = {}

for word in words:
    if word in count_words:
        count_words[word] = count_words[word] + 1
    else:
        count_words[word] = 1

for word in count_words:
    print(word, ":", count_words[word])