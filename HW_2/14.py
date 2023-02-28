n = int(input('Введите число: '))
list = [2**i for i in range (n) if 2**i <= n ]
print(list)