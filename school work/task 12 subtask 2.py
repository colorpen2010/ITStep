try:
    prc = float(input("Введите цену товара: "))
    disc = float(input("Введите процент скидки: "))

    final_prc = prc - (prc * disc / 100)

    print("Финальная цена:", final_prc)

except ValueError:
    print("Ошибка ввода! Нужно вводить числа.")