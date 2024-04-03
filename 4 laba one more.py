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
div5()

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
div300()

def mag(x):
    day, month, year = map(int, x.split('.'))
    if day * month == year % 100:
        y = "it's magic date, bro"
    else:
        y = "this is not a magic date "
    return y
x = input("Введите дату в формате 'дд.мм.гггг':" )
print(mag(x))
mag()



def z4():
    def happy(x):
        sum1 = 0
        for i in range(len(x) // 2):
            sum1 += int(x[i])
        sum2 = 0
        for j in range(len(x) // 2, len(x)):
            sum2 += int(x[j])
        if sum1 == sum2:
            return "билет счастливый"
        else:
            return "повезет в другой раз"
    x = input("введите номер билета: ")
    if len(x) % 2 == 0:
        print(happy(x))
    else:
        print("Перезапустите программу и введите номер билета еще раз. В номере билета должно быть четное количество цифр!")
z4()