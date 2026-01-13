a = float(input("введите количество метров: "))
b = input("выберите режим. one, two или three: ")

if b == "one":
    unit = input("введите тип, miles или inches или yards: ")  # miles, inches, yards

    if unit == "miles":
        print(a / 1609)
    elif unit == "inches":
        print(a * 39.37)
    elif unit == "yards":
        print(a * 1.094)

elif b == "two":
    print(a / 1609)
    print(a * 39.37)
    print(a * 1.094)

elif b == "three":
    print(a / 1000)
    print(a * 100)

