def count_dig(nmbr):

    txt = str(nmbr)
    cnt = 0

    for ch in txt:
        cnt = cnt + 1

    return cnt


res = count_dig(3456)
print("Количество цифр:", res)