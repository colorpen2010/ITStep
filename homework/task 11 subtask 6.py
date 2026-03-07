def lucky_nmbr(nmbr):

    txt = str(nmbr)

    s1 = int(txt[0]) + int(txt[1]) + int(txt[2])
    s2 = int(txt[3]) + int(txt[4]) + int(txt[5])

    if s1 == s2:
        return True
    else:
        return False


res = lucky_nmbr(123420)

if res == True:
    print("Число счастливое")
else:
    print("Число не счастливое")