try:
    f = open("log.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("log.txt не найден, создаю файл...")
    f = open("log.txt", "w", encoding="utf-8")
    f.write("Sciense is not about why, it's about.....    actually science is really why...\n")
    f.close()
    f = open("log.txt", "r", encoding="utf-8")

txt = f.read().lower()
f.close()

words = txt.split()

d = {}

for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1

items = list(d.items())
items.sort(key=lambda x: x[1], reverse=True)

f2 = open("word_stats.txt", "w", encoding="utf-8")

for i in range(10):
    if i < len(items):
        w, cnt = items[i]
        f2.write(w + " - " + str(cnt) + "\n")

f2.close()

print("Топ слов записан")