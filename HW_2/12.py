S = int(input('Введите сумму чисел: '))
P = int(input('Введите произведение чисел: '))
for x in range(S):
    for y in range(P):
        if S == x + y and P == x * y:
            print(x, y)