def get_rez(a):
    if a % 3 == 0:
        return "Число делится на три."
    else:
        return "Число не делится на три."
a = int(input("Введите число: "))
print(get_rez(a))
