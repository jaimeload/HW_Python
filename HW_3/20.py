w = input("Введите слово: ")
word = str.upper(w)
print(word)
dct = {1:"AEIOULNSTRАВЕИНОРСТ", 2:"DGДКЛМПУ", 3:"BCMPБГЁЬЯ", 4:"FHVWYЙЫ", 5:"KЖЗХЦЧ", 8:"JXШЭЮ", 10:"QZФЩЪ"}
print(sum([i for letter in word for i, val in dct.items() if letter in val]))