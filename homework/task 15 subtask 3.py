while True:

    print("\nМеню:")
    print("1 - Добавить заказ")
    print("2 - Показать все")
    print("3 - Поиск по номеру")
    print("4 - Обновить заказ")
    print("5 - Удалить заказ")
    print("0 - Выход")

    ch = input("Выбор: ")

    # ➜ Добавить
    if ch == "1":
        num = input("Номер: ")
        name = input("Товар: ")
        qty = input("Количество: ")
        prc = input("Цена: ")

        f = open("orders.txt", "a", encoding="utf-8")
        f.write(num + "," + name + "," + qty + "," + prc + "\n")
        f.close()

        print("Заказ добавлен")

    # ➜ Показать
    elif ch == "2":
        try:
            f = open("orders.txt", "r", encoding="utf-8")
            print(f.read())
            f.close()
        except:
            print("Файл пуст или не найден")

    # ➜ Поиск
    elif ch == "3":
        num = input("Введите номер: ")

        try:
            f = open("orders.txt", "r", encoding="utf-8")

            found = False

            for line in f:
                if num in line:
                    print(line.strip())
                    found = True

            if not found:
                print("Заказ не найден")

            f.close()
        except:
            print("Ошибка чтения файла")

    # ➜ Обновить
    elif ch == "4":
        num = input("Введите номер: ")

        try:
            f = open("orders.txt", "r", encoding="utf-8")
            lines = f.readlines()
            f.close()

            f = open("orders.txt", "w", encoding="utf-8")

            for line in lines:
                if num in line:
                    print("Найден заказ:", line.strip())
                    qty = input("Новое количество: ")
                    prc = input("Новая цена: ")

                    parts = line.strip().split(",")
                    new_line = parts[0] + "," + parts[1] + "," + qty + "," + prc + "\n"

                    f.write(new_line)
                else:
                    f.write(line)

            f.close()
            print("Обновление завершено")

        except:
            print("Ошибка")

    # ➜ Удалить
    elif ch == "5":
        num = input("Введите номер: ")

        try:
            f = open("orders.txt", "r", encoding="utf-8")
            lines = f.readlines()
            f.close()

            f = open("orders.txt", "w", encoding="utf-8")

            for line in lines:
                if num not in line:
                    f.write(line)

            f.close()
            print("Удаление завершено")

        except:
            print("Ошибка")

    elif ch == "0":
        print("Выход")
        break