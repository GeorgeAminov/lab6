def get_rez(a):
    if a % 3 == 0:
        return "Число делится на три."
    else:
        return "Число не делится на три."

def get_delsto(a):
    rez = 100 / a
    return rez

def get_magic(a, b, c):
    yeartwo = int(str(c)[-2:])
    return (a * b) == yeartwo

def get_lucky(a):
    first_sum = 0
    second_sum = 0
    half = len(a) // 2
    first_half = a[:half]
    second_half = a[half:]
    for i in first_half:
        first_sum += int(i)
    for i in second_half:
        second_sum += int(i)
    if first_sum == second_sum:
        return "Это счастливый билетик."
    else:
        return "Это не счастливый билетик."

def task_1():
    try:
        a = int(input("Введите число: "))
        print(get_rez(a))
    except:
        print("Введите корректное число.")

def task_2():
    while True:
        try:
            number = int(input("Введите число: "))
            print(get_delsto(number))
            break
        except ValueError:
            print("Делить можно только на число!")
        except ZeroDivisionError:
            print("Нельзя делить на ноль!")

def task_3():
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
    print(get_magic(day, month, year))

def task_4():
    try:
        number = input("Введите номер билета: ")
        if int(number) < 0:
            print("Цифры в билетеке должны быть положительными.")
        elif len(number) % 2 == 0:
            print(get_lucky(number))
        else:
            print("В билетике должно быть чётное количество циферок.")
    except:
        print("Ошибка!")

task_1()
#task_2()
#task_3()
#task_4()