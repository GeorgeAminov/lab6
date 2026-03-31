def magic(a, b, c):
    return (a * b) == c
while True:
    try:
        day = int(input("Введите день: "))
        if day < 1 or day > 31:
            print("Ошибка!")
            continue
        break
    except:
        print("Ошибка!")
while True:
    try:
        month = int(input("Введите месяц: "))
        if month < 1 or month > 12:
            print("Ошибка!")
            continue
        break
    except:
        print("Ошибка!")
while True:
    try:
        year = int(input("Введите год: "))
        break
    except:
        print("Ошибка!")
yeartwo=int(str(year)[-2:])
print(magic(day, month, yeartwo))
