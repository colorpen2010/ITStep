def power(nmbr, pwr):

    if pwr == 0:
        return 1

    return nmbr * power(nmbr, pwr - 1)


res = power(2, 5)

print("Результат:", res)