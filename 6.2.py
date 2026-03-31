def get_delsto(a):
    rez = 100 / a
    return rez
while True:
    try:
        number = int(input("Введите число: "))
        print(get_delsto(number))
        break
    except ValueError:
        print("Делить можно только на число!")
    except ZeroDivisionError:
        print("Нельзя делить на ноль!")
    except:
        print("Ошибка.")