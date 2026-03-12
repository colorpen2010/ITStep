import random

lst = []

for i in range(100):
    lst.append(random.randint(1, 100))

print("Список создан")


def find_min(lst, pos, best_pos, best_sum):

    if pos > 90:
        return best_pos

    s = 0
    for i in range(pos, pos + 10):
        s = s + lst[i]

    if best_sum == -1 or s < best_sum:
        best_sum = s
        best_pos = pos

    return find_min(lst, pos + 1, best_pos, best_sum)


res = find_min(lst, 0, 0, -1)

print("Позиция начала минимальной суммы:", res)