from figures import Circle, Rectangle, Triangle

while True:
    print("\n1 - Коло")
    print("2 - Прямокутник")
    print("3 - Трикутник")
    print("0 - Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        r = float(input("Радіус: "))
        c = Circle(r)
        print("Площа:", c.area())
        print("Периметр:", c.perimetr())

    elif choice == "2":
        a = float(input("Сторона 1: "))
        b = float(input("Сторона 2: "))
        r = Rectangle(a, b)
        print("Площа:", r.area())
        print("Периметр:", r.perimetr())

    elif choice == "3":
        a = float(input("Сторона 1: "))
        b = float(input("Сторона 2: "))
        c = float(input("Сторона 3: "))
        t = Triangle(a, b, c)
        print("Площа:", t.area())
        print("Периметр:", t.perimetr())

    elif choice == "0":
        break