# Secuencia ordenada de objetos

lista = ['Hola',20,'World',6.1]
r =(len(lista)) # ver el largo de la lista
print(r)

# extraer el valor de unos de sus elementos # indexar
r = lista[0:2] # de 0 hasta 2
print(r)

# Unir listas
lista2 = ['Python',2]
print(lista+lista2)

lista3 = lista + lista2 # Crear una lista nueva
print(lista3)

# Remplazar algo de una lista, concatenacion

lst4 = lista3
lst4[0] = 'alfa'
print(lst4)

# agregar un elemento, la lista de origen es modificada
lst4.append('Nuevo')
print(lst4)

# eliminar un elemento
lst4.pop(2) # si no dejas nada, elimina el ultimo de los elementos
print(lst4)

# tambien se puede almacenar el elemento eliminado en una variable
eliminado = lst4.pop(0)
print(eliminado)

# Ordenar una lista
lst5 = ['d','c','a','b','f','e']
lst5.sort() # Es un metodo que trabaja en el lugar, pero no devuelve nada
lst5_ordenada = lst5 # asi es que se guarda una lista ordenada
print(lst5)

lst5.reverse() # al igual que short no devuelve nada
print(lst5) # la muestra al revez, pero alfabeticamente ordenada por el metodo anterior