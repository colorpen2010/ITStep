nums = list(map(int, input("Введите числа: ").split()))

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        print("Индекс четного числа:", i)
