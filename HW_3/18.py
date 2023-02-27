from random import randint
n = int(input("Введите количество элементов: "))
x = int(input("Введите число: "))
lst = [randint(1, 7) for i in range(n)]
nearest = min(lst, key=lambda i:abs(i - x))
print(lst)
print(f'{nearest} ближайшее число к {x}')