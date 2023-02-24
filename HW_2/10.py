n = int(input('Введите количество монет: '))
count0 = 0
count1 = 0
for i in range(n):
    x = int(input('Введите сторону монеты (0 - Орёл, 1 - Решка): '))
    if x == 0:
        count0 += 1
    else:
        count1 += 1
if count1 > count0:
    print(f'{count0} монет нужно перевернуть, чтобы все лежали одной стороной')
else:
    print(f'{count1} монет нужно перевернуть, чтобы все лежали одной стороной')