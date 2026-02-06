size = int(input("Введіть розмір фігури: "))

print("Меню:")
print("1 - Діагональ \\")
print("2 - Діагональ /")
print("3 - Хрест")
print("4 - Верхній трикутник")
print("5 - Нижній трикутник")

choice = int(input("Ваш вибір: "))


for i in range(size):
    for j in range(size):

        if choice == 1:
            if i == j:
                print("*", end="")
            else:
                print(" ", end="")

        elif choice == 2:
            if i + j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")

        elif choice == 3:
            if i == j or i + j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")

        elif choice == 4:
            if i <= j:
                print("*", end="")
            else:
                print(" ", end="")

        elif choice == 5:
            if i >= j:
                print("*", end="")
            else:
                print(" ", end="")

    print()
