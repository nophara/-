'''
def div5(x):
    if x % 5 == 0:
        return True
    else:
        return False
x = int(input("Введите любое число"))
if div5(x):
    print(f"{x} делится на 5")
else:
   print(f"{x}) не делится на 5")


def div300(x):
    zadacha = 300 / x
    return zadacha
try:
    x = int(input("Введите число:"))
    print(div300(x))
except ValueError:
    print("Опа, Ошибочка! Это ведь не число")
except ZeroDivisionError:
    print("Эх ты. Деление на ноль невозможно:")
'''
def mag(x):
    day, month, year = map(int, x.split('.'))
    if day * month == year % 100:
        y = "it's magic date, bro"
    else:
        y = "this is not a magic date "
    return y
x = input("Введите дату в формате 'дд.мм.гггг':" )
print(mag(x))


