word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

set1 = set(word1)
set2 = set(word2)

if set1 == set2:
    print("Слова являються анаграммами")
else:
    print("Слова НЕ являються анаграммами")