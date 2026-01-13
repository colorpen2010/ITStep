a = float(input())
b = float(input())
c = float(input())

choice = input("max или min или mid: ")  # max, min, avg

if choice == "max":
    print(max(a, b, c))
elif choice == "min":
    print(min(a, b, c))
elif choice == "mid":
    print((a + b + c) / 3)
