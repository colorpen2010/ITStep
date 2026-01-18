inpt=float(input("Введите балл от 0 до 100: "))
if inpt>100 or inpt<0:
    raise ValueError("Неправильное число")
if inpt>=90:
    print("Відмінно")
elif inpt>=70:
    print("Добре")
elif inpt>=50:
    print("Задовільно")
elif inpt<50:
    print("Незадовільно")