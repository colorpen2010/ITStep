def is_pal(nmbr):

    txt = str(nmbr)

    rev = ""

    for ch in txt:
        rev = ch + rev

    if txt == rev:
        return True
    else:
        return False


res = is_pal(123321)

if res == True:
    print("Число палиндром")
else:
    print("Число не палиндром")