balance = 1000

try:
    amt = int(input("Введите сумму для снятия: "))

    if amt % 10 != 0:
        raise Exception("Сумма должна быть кратна 10")

    if amt > balance:
        raise Exception("Недостаточно средств")

    print("Вы сняли:", amt)

except ValueError:
    print("Ошибка! Введите число.")

except Exception as e:
    print("Ошибка:", e)

finally:
    print("Транзакция завершена")