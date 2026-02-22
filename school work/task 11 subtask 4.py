dictionary = {
    "cat": "кот",
    "dog": "пёс",
    "house": "дом",
    "sun": "солнце",
    "book": "книга"
}

word = input("Введите слово английским: ")

if word in dictionary:
    print("Перевод:", dictionary[word])
else:
    print("Слово не найдено")