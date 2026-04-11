class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def show_grades(self):
        print(f'Grades of {self.name}: {self.grades}')

    def __str__(self):
        return f'Name: {self.name} {self.surname}\nAge: {self.age}\nGrades: {self.grades}'