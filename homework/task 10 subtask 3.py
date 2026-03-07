def draw_sq(size, symb, fill):

    for i in range(size):

        if fill == True:
            print(symb * size)

        else:

            if i == 0 or i == size - 1:
                print(symb * size)

            else:
                print(symb + " " * (size - 2) + symb)


draw_sq(5, "*", True)
print()
draw_sq(5, "#", False)