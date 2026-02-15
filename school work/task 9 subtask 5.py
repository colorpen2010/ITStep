nums = list(map(int, input("Введите числа: ").split()))
# split() — делит строку по пробелам  
# map(int, ...) — превращает части в числа  
# list(...) — делает список

unique = []

for n in nums:
    if nums.count(n) == 1:
        # count(n) — считает сколько раз число n есть в списке

        unique.append(n)
        # append(...) — добавляет элемент в список

print("Уникальные:", unique)