while True:

    print("\nМеню:")
    print("1 - Добавить альбом")
    print("2 - Показать все")
    print("3 - Поиск по исполнителю")
    print("4 - Удалить альбом")
    print("0 - Выход")

    ch = input("Выбор: ")

    # ➜ Добавить
    if ch == "1":
        name = input("Название альбома: ")
        art = input("Исполнитель: ")
        yr = input("Год: ")

        f = open("music_collection.txt", "a")
        f.write(name + "," + art + "," + yr + "\n")
        f.close()

        print("Альбом добавлен")

    # ➜ Показать всё
    elif ch == "2":
        f = open("music_collection.txt", "r")

        txt = f.read()
        print(txt)

        f.close()

    # ➜ Поиск
    elif ch == "3":
        art = input("Введите исполнителя: ")

        f = open("music_collection.txt", "r")

        for line in f:
            if art in line:
                print(line.strip())

        f.close()

    # ➜ Удаление
    elif ch == "4":
        name = input("Введите название альбома: ")

        f = open("music_collection.txt", "r")
        lines = f.readlines()
        f.close()

        f = open("music_collection.txt", "w")

        for line in lines:
            if name not in line:
                f.write(line)

        f.close()

        print("Удаление завершено")

    elif ch == "0":
        print("Выход")
        break