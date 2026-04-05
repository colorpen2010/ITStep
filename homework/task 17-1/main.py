from students import Student
from car import Car

student = Student("Іван", "Петров", 20)
car = Car("Toyota", "Camry", 180, 2020)

while True:
    print("\n1 - Показати студента")
    print("2 - Додати оцінку")
    print("3 - Показати оцінки")
    print("4 - Показати авто")
    print("0 - Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        print(student)

    elif choice == "2":
        grade = int(input("Введіть оцінку: "))
        student.add_grade(grade)

    elif choice == "3":
        student.show_grades()

    elif choice == "4":
        car.show_info()

    elif choice == "0":
        break