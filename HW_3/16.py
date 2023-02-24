# Решил что с рандомными числами задача будет поинтереснее

from random import randint
n = int(input("Введите количество элементов: "))
x = int(input("Введите число: "))
lst = [randint(0, 5) for i in range(n)]
count = 0
for item in lst:
    if item == x:
        count += 1
print(lst)
print(f'{x} встречается {count} раз')