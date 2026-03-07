def max4(a, b, c, d):

    mx = a

    if b > mx:
        mx = b

    if c > mx:
        mx = c

    if d > mx:
        mx = d

    return mx


res = max4(4, 9, 2, 7)
print("Максимальное число:", res)