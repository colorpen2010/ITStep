from shapes import *

while True:
    print('\n1 - Circle')
    print('2 - Rectangle')
    print('3 - Triangle')
    print('0 - Exit')

    choice = input('Choose: ')

    if choice == '1':
        r = float(input('Radius: '))
        circle = Circle(r)

        print('Area:', circle.area())
        print('Perimeter:', circle.perimetr())

    elif choice == '2':
        w = float(input('Width: '))
        h = float(input('Height: '))
        rect = Rectangle(w, h)

        print('Area:', rect.area())
        print('Perimeter:', rect.perimetr())

    elif choice == '3':
        a = float(input('Side a: '))
        b = float(input('Side b: '))
        c = float(input('Side c: '))

        tri = Triangle(a, b, c)

        print('Area:', tri.area())
        print('Perimeter:', tri.perimetr())

    elif choice == '0':
        break