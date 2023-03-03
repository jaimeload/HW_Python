A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))
def summa(a, b):
    if b == 0:
        return a
    else:
        return summa(a, b - 1) + 1
print(summa(A, B))