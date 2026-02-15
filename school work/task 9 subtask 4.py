nums_str = input("Введите числа: ").split()

nums = []
for n in nums_str:
    nums.append(int(n))

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        print("Індекс:", i)