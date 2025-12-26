price_per_day = float(input("ведите число: "))
days = float(input("ведите число: "))
deposit = float(input("ведите число: "))

rent_cost = price_per_day * days
total_with_deposit = rent_cost + deposit
after_return = rent_cost
per_day = rent_cost / days

print(total_with_deposit)
print(after_return)
print(per_day)
