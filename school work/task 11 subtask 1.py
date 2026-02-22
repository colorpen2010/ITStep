contacts = {}

while True:
    print("\nМеню:")
    print("1 - Добавить контакт")
    print("2 - Удалить контакт")
    print("3 - Изменить контакт")
    print("4 - Показать все контакты")
    print("0 - Выйти")

    choice = input("Ваш выбор: ")

    if choice == "1":
        name = input("Имя: ")
        phone = input("Телефон: ")
        contacts[name] = phone
        print("Контакт добавлен")

    elif choice == "2":
        name = input("Имя контакта для удаления: ")
        if name in contacts:
            del contacts[name]
            print("Контакт удалён")
        else:
            print("Контакт не найден")

    elif choice == "3":
        name = input("Имя контакта для изменения: ")
        if name in contacts:
            phone = input("Новый телефон: ")
            contacts[name] = phone
            print("Контакт изменён")
        else:
            print("Контакт не найден")

    elif choice == "4":
        if contacts == {}:
            print("Контактов нет")
        else:
            for name in contacts:
                print(name, ":", contacts[name])

    elif choice == "0":
        print("Выход из программы")
        break

    else:
        print("Неверный выбор")