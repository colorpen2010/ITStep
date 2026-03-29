f1 = open("data.txt", "r")
f2 = open("encrypted.txt", "w")

txt = f1.read()

res = ""

for ch in txt:

    if ch.isalpha():

        if ch == "z":
            res = res + "a"
        elif ch == "Z":
            res = res + "A"
        else:
            res = res + chr(ord(ch) + 1)

    else:
        res = res + ch

f2.write(res)

f1.close()
f2.close()

print("Файл зашифрован")