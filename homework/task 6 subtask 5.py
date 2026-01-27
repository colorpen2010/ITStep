start = int(input("введите начальное число: "))
end = int(input("введите конечное число: "))

if start > end:
    start, end = end, start

product = 1
found = False

for i in range(start, end + 1):
    if i % 4 == 0 and i % 6 != 0:
        product *= i
        found = True

if found:
    print(product)
else:
    print("Таких чисел нету")
