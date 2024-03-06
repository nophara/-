import random
n = 0
m = 0
nasd = 0
while n < 3:
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = int(input(f"{a} + {b} ="))
    if a + b == c:
        print('правильно!')
        m+=1
    else:
        print('отет неверный')
        n+=1
print('Игра окончена. Верных ответо:', m)