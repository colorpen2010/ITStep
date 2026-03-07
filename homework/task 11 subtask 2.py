def odd_nmbrs(a, b):

    for nmbr in range(a, b + 1):

        if nmbr % 2 != 0:
            print(nmbr)

odd_nmbrs(3, 15)