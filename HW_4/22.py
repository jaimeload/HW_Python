from random import randint
n = int(input("Введите количество элементов первого набора чисел: "))
m = int(input("Введите количество элементов второго набора чисел: "))
lst1 = [randint(1, 20) for i in range(n)]
lst2 = [randint(1, 20) for i in range(m)]
lst3 = set()
print(lst1)
print(lst2)
for i in lst1:
    for j in lst2:
        if i in lst2:
            lst3.add(i)
print([lst3])