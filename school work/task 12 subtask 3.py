try:
    usd = float(input("Введите сумму в долларах: "))
    rate = float(input("Введите курс евро: "))

    if rate == 0:
        raise Exception("Курс обмена не может быть нулем")

    eur = usd / rate

    print("Сумма в евро:", eur)

except ValueError:
    print("Ошибка ввода! Нужно вводить числа.")

except Exception as e:
    print("Ошибка:", e)

finally:
    print("Операция завершена")