# FUNCION, hace mas facil acceder a los indices de una coleccion
lista = ["a", "b", "c"]
indice = 0

# Por cada item en lista, imprime el indice y el elemento de la lista
# esto es una forma no tan eficiente en py
for item in lista:
    print(indice, item)
    indice += 1  # suma +1 en cada vuelta del loop


# con indice
for item in enumerate(lista):
    print(item)  # contiene una tupla, con el indice y el objeto

# tambien se puede separar en dos variables
for indice, item in enumerate(
    lista
):  # tambien podes poner un rango dentro de un enumerate(range(10,55))
    print(indice, item)

# tambien se utiliza fuera de un loop
# Nuestra lista, convertirla en un tuple
tuples = list(enumerate(lista))
print(tuples[1][0])
