from random import randint
n = int(input("Введите количество элементов первого набора чисел: "))
m = int(input("Введите количество элементов второго набора чисел: "))
lst1 = [randint(1, 20) for i in range(n)]
lst2 = [randint(1, 20) for i in range(m)]
print(lst1)
print(lst2)
set3 = set([i for i in lst1 for j in lst2 if i in lst2])
lst3 = list(set3)
print(lst3)
