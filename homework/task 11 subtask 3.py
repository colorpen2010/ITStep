def draw_line(lng, dir, symb):

    if dir == "h":

        for i in range(lng):
            print(symb, end="")

        print()

    elif dir == "v":

        for i in range(lng):
            print(symb)


draw_line(8, "h", "*")
print()
draw_line(5, "v", "#")