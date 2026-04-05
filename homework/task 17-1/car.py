class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def show_info(self):
        print("Бренд:", self.brand)
        print("Модель:", self.model)
        print("Швидкість:", self.speed)
        print("Рік:", self.year)