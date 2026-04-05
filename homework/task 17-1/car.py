class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def show_info(self):
        print(self)

    def __str__(self):
        return f'Brand: {self.brand}\nModel: {self.model}\nSpeed: {self.speed}\nYear: {self.year}'