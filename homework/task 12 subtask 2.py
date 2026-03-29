def leap(yr):
    if yr % 4 == 0 and yr % 100 != 0:
        return True
    if yr % 400 == 0:
        return True
    return False


def days_in_mnth(mnth, yr):

    if mnth == 2:
        if leap(yr):
            return 29
        else:
            return 28

    if mnth == 4 or mnth == 6 or mnth == 9 or mnth == 11:
        return 30

    return 31


def date_to_days(d, m, y):

    days = d

    for yr in range(1, y):
        if leap(yr):
            days = days + 366
        else:
            days = days + 365

    for mnth in range(1, m):
        days = days + days_in_mnth(mnth, y)

    return days


def diff_dates(d1, m1, y1, d2, m2, y2):

    days1 = date_to_days(d1, m1, y1)
    days2 = date_to_days(d2, m2, y2)

    diff = days2 - days1

    if diff < 0:
        diff = -diff

    return diff


d1 = int(input("Введите день первой даты: "))
m1 = int(input("Введите месяц первой даты: "))
y1 = int(input("Введите год первой даты: "))

d2 = int(input("Введите день второй даты: "))
m2 = int(input("Введите месяц второй даты: "))
y2 = int(input("Введите год второй даты: "))

res = diff_dates(d1, m1, y1, d2, m2, y2)

print("Разница в днях:", res)