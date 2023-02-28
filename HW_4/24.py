from random import randint
n = int(input("Введите количество грядок: "))
lst = [randint(1, 7) for i in range(n)]
print(lst)
lsts = []
for i in range(n - 1):
    lsts.append(lst[i] + lst[i - 1] + lst[i + 1])
lsts.append(lst[0] + lst[-1] + lst[-2])
print(max(lsts))