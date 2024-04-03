def zadacha1():
    chisla = [3, 5, 17, 23, 37]
    n = int(input('введите число: '))
    if n in chisla:
        print('исходный список: ', chisla)
        print('введенное число: ', n)
        print('Поздравляю, Вы угадали число!')
    else:
        print('сходный список: ', chisla)
        print('введенное число: ', n)
        print('Нет такого числа!')
zadacha1()
def zadacha2():
    chisla = [1,2,3,4,1,6,7,8,3,6]
    povtori = set([x for x in chisla if chisla.count(x) > 1])
    print('повторяющихся чисел в списке: ', povtori)
zadacha2()

def zadacha3():
    dni = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
    chill = int(input('сколько выходных дней вы хотите иметь на неделе? '))
    weekends = dni[-chill:]
    rabota = dni[:-chill]
    print('ваши выходные дни: ', weekends)
    print('ваши рабочие дни: ', rabota)
zadacha3()



def zadacha4():
    group20 = ['Иванов', 'Петров', 'Шишкин', 'Свиридов', 'Фалалеева', 'Абрамов', 'Виноградова', 'Зверев', 'Левкин',
                   'Воробьев']
    group25 = ['Абрамов', 'Карекина', 'Малоземов', 'Рябова', 'Гусев', 'Щепилов', 'Тарасенко', 'Ринне', 'Дорохин',
                   'Ли']
    football = tuple(group20[:5] + group25[:5])
    print('группа 20: ', group20)
    print('группа 25: ', group25)
    print('футбольная команда: ', football)
    print(len(football))
    football = sorted(football)
    print(football)
    gusev = football.count('Абрамов')
    print('в команде с фамилией "Абрамов" ',gusev, ' человек(a)')
zadacha4()
