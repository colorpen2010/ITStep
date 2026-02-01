shape = input("выберите square или rectangle: ")  # square або rectangle
symbol = input("введите символ: ")

if shape == "square":
    size = float(input("введите размер: "))

    for i in range(size):
        print(symbol * size)

elif shape == "rectangle":
    width = int(input("введите ширину: "))
    height = int(input("введите высоту: "))

    for i in range(height):
        print(symbol * width)

