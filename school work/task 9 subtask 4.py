nums = list(map(int, input("Введите числа: ").split()))

for i in range(len(nums)):
    # range() — создаёт последовательность чисел от 0 до указанного числа (не включая его)
    # len(nums) — длина списка

    if nums[i] % 2 == 0:
        # % — остаток от деления
        print("Індекс:", i)
