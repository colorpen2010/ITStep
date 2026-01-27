start = int(input("введите начальное число: "))
end = int(input("введите конечное число: "))
step = int(input("введите размер шага: "))
order = input("выберите forward или backward: ")

if order == "forward":
    for i in range(start, end + 1, step):
        print(i)

elif order == "backward":
    for i in range(end, start - 1, -step):
        print(i)
