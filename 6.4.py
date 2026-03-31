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
try:
    number = input("Введите номер билета: ")
    if int(number) < 0:
        print("Цифры в билетеке должны быть положительными.")
    elif len(number) % 2 == 0:
        print(get_lucky(number))
    else:
        print("В билетике должно быть чётное количество циферок.")
except:
    print ("Ошибка!")