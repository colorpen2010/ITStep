text = input("Введите рядок: ")
a = input("Первый символ: ")
b = input("Второй символ: ")

start = -1
end = -1

for i in range(len(text)):
    if text[i] == a and start == -1:
        start = i
    if text[i] == b and end == -1:
        end = i

if start != -1 and end != -1 and start < end:
    result = text[:start] + text[end+1:]
else:
    result = text

print(result)
