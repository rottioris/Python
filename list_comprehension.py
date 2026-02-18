palabra = "Python"

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# Con comprension
lista = [letra for letra in "Python"]


lst = [n for n in range(0, 40, 2)]
print(lst)

lst2 = [n / 2 for n in range(0, 20, 2)]
print(lst2)

lst3 = [n if n * 2 > 10 else "X" for n in range(0, 20, 2)]
print(lst3)


pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)