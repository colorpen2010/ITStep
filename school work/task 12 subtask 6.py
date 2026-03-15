try:
    ord_nm = input("Введите номер заказа: ")

    if ord_nm[:3] != "ORD":
        raise Exception("Номер должен начинаться с ORD")

    num = ord_nm[3:]

    if num == "" or not num.isdigit():
        raise Exception("После ORD должны быть цифры, между ORD и цифрами не должно быть пробелов")

    print("Номер заказа корректный")

except Exception as err:
    print("Ошибка:", err)

finally:
    print("Проверка завершена")