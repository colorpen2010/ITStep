def sym_list(lst):

    if len(lst) <= 1:
        return True

    if lst[0] != lst[-1]:
        return False

    return sym_list(lst[1:-1])


lst = [1, 2, 3, 2, 1]

if sym_list(lst):
    print("Список симметричный")
else:
    print("Список не симметричный")