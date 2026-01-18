salat = float(input("Введіть заробітну плату: "))
exper = float(input("Введіть стаж роботи (у роках): "))

if exper < 1:
    print("Премія не передбачена")
elif exper < 3:
    print("Премія:", salat * 0.05)
elif exper < 5:
    print("Премія:", salat * 0.10)
else:
    print("Премія:", salat * 0.15)
