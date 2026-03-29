f = open("data.txt", "w", encoding="utf-8")

for i in range(3):
    txt = input("Введите строку: ")
    f.write(txt + "\n")

f.close()

print("Данные записаны в файл")