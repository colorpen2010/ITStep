distance = float(input("ведите число: "))
fuel_per_100 = float(input("ведите число: "))
price_per_liter = float(input("ведите число: "))

fuel_used = distance * fuel_per_100 / 100
cost = fuel_used * price_per_liter

print(cost)
