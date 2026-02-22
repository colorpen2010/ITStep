rates = {
    "USD": 40.2,
    "EUR": 42.5,
    "PLN": 9.6
}

currency = input("Введите валюту (USD, EUR, PLN): ")
uah = float(input("Введите сумму в гривнах: "))

if currency in rates:
    result = uah / rates[currency]
    print("Результат:", result, currency)
else:
    print("Такой валюты нет")