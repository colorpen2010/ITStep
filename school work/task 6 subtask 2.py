start = int(input("введите начальное число: "))
end = int(input("введите конечное число: "))

for i in range(start, end + 1):
    print(i)

for i in range(end, start - 1, -1):
    print(i)

for i in range(start, end + 1):
    if i % 7 == 0:
        print(i)

count = 0

for i in range(start, end + 1):
    if i % 5 == 0:
        count += 1

print(count)
