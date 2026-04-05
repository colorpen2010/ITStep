class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} років"

    def show_grades(self):
        print("Оцінки:", self.grades)

    def add_grade(self, grade):
        self.grades.append(grade)