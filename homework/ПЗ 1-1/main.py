from student import *
from car import *

student = Student('Ivan', 'Petrov', 18)
car = Car('BMW', 'M5', 250, 2020)

while True:
    print('\n1 - Student')
    print('2 - Car')
    print('0 - Exit')

    choice = input('Choose: ')

    if choice == '1':
        print('\n1 - Show student')
        print('2 - Add grade')
        print('3 - Show grades')

        s = input('Choose: ')

        if s == '1':
            print(student)

        elif s == '2':
            grade = int(input('Enter grade: '))
            student.add_grade(grade)

        elif s == '3':
            student.show_grades()

    elif choice == '2':
        car.show_info()

    elif choice == '0':
        break