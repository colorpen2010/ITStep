start = float(input("введите начальное число: "))
end = float(input("введите конечное число: "))

for i in range(start, end + 1):
    if i % 7 == 0:
        print(i)
