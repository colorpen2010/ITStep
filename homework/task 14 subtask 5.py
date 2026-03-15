try:
    txt = input("Введите товар (название, цена, количество): ")

    parts = txt.split(",")

    name = parts[0].strip()
    prc = float(parts[1])
    qty = int(parts[2])

    print("Товар:", name)
    print("Цена:", prc)
    print("Количество:", qty)

except ValueError:
    print("Ошибка! Цена или количество введены неправильно.")

finally:
    print("Парсинг завершен")