import random

set1 = set()
set2 = set()

while len(set1) < 10:
    set1.add(random.randint(1, 20))

while len(set2) < 10:
    set2.add(random.randint(1, 20))

print("Множество 1:", set1)
print("Множество 2:", set2)

print("Общие элементы:", set1 & set2)

print("Разница:", set1 - set2)

print("Объединение:", set1 | set2)