total = 0
discount = 0
drink = ""

snack = input("Оберіть закуску (Салат / Суп / Нічого): ")

if snack == "Салат":
    total += 5
elif snack == "Суп":
    total += 7

main = input("Оберіть основну страву (Курка / Риба / Нічого): ")

if main == "Курка":
    total += 10
elif main == "Риба":
    total += 12

dessert = input("Оберіть десерт (Морозиво / Фрукти / Нічого): ")

if dessert == "Морозиво":
    total += 3
elif dessert == "Фрукти":
    total += 4

if snack != "Нічого" and main != "Нічого" and dessert != "Нічого":
    discount = 0.10

if total > 20:
    discount = 0.15

regular = input("Ви постійний клієнт? (так / ні): ")

if regular == "так":
    discount += 0.05

if snack == "Суп" and main == "Риба" and dessert != "Нічого":
    total -= 2

if main == "Курка" and dessert == "Морозиво":
    drink = "Безкоштовний напій: Чай"

total = total - (total * discount)

print("Підсумкова вартість:", total, "$")

if drink != "":
    print(drink)
