width = int(input("Введите ширину прямоугольника: "))
height = int(input("Введите высоту прямоугольника: "))

for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")
