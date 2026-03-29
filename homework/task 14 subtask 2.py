lst = [10, 20, 30, 40, 50]

try:
    ind = int(input("Введите индекс элемента: "))

    print("Элемент списка:", lst[ind])

except ValueError:
    print("Ошибка! Индекс должен быть числом.")

except IndexError:
    print("Ошибка! Индекс выходит за пределы списка.")

finally:
    print("Операция завершена")