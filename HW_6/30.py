a = int(input("Введите начало прогрессии: "))
k = int(input("Введите шаг прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))
lst = [i for i in range(a, (a + ((n - 1) * k) + 1), k)]
print(lst)