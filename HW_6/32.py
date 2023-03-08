from random import randint
n = int(input("Введите количество элементов массива: "))
a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
lst = [randint(-20, 20) for i in range(n)]
print(lst)
for i in range(len(lst)):
    if a < lst[i] < b:
        print(i, end=' ')