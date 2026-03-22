try:
    f1 = open("data.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Файл не найден, создаю новый...")
    f1 = open("data.txt", "w", encoding="utf-8")
    f1.write("https://www.pinterest.com/pin/4785143350078240/\n")
    f1.close()
    f1 = open("data.txt", "r", encoding="utf-8")

txt = f1.read()
f1.close()

f2 = open("backup.txt", "w", encoding="utf-8")
f2.write(txt)
f2.close()

print("Копирование завершено")