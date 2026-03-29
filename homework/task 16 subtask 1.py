import random

name = input("Введите имя: ")

# Вариант 1
nick1 = name + str(random.randint(100, 9999))

# Вариант 2
letters = "abcdefghijklmnopqrstuvwxyz"
symbols = ["_", ".", "-"]

random_letters = ""
for i in range(3):
    random_letters += random.choice(letters)

nick2 = name + random.choice(symbols) + random_letters

# Вариант 3
prefixes = ["Pro", "Super", "Ultra", "Mega", "For Queen!", "Hyper"]
nick3 = random.choice(prefixes) + name.capitalize() + str(random.randint(10, 99))

print("\nВаши никнеймы:")
print(nick1)
print(nick2)
print(nick3)