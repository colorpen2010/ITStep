import random

secret = random.randint(1, 500)
attempts = 0

while True:
    guess = float(input("введите число: "))

    if attempts >= 12:
        print("игра законченна")
        break

    attempts += 1

    if guess < secret:
        print("больше")
    elif guess > secret:
        print("Меньше")
    else:
        print("Угадано за", attempts, "попыток")
        break
