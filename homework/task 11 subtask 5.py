def is_prime(nmbr):

    if nmbr < 2:
        return False

    for i in range(2, nmbr):

        if nmbr % i == 0:
            return False

    return True


res = is_prime(7)

if res == True:
    print("Число простое")
else:
    print("Число не простое")