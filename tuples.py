# las tuples son inmutabdles, aun mas limitados que las listas, pero ocupan menos espacio de memoria y al no poder ser modificadas se utilizan para almacenar estructuras que no quieres que se modifiquen

mi_tuple = 1,2,3,4 # fucniona con (1,2,3) o sin parentesis 1,2,3
print(type(mi_tuple))

t = (5,2.34,'gg') # puede contener varios valores

# indexar
print(mi_tuple[0]) 

# Recordad que los tuples no soportan asignacion de items, pero si se pueden anidar

tp = (1,2,(10,20),3)
print(tp[2][0])

# casting
tp = list(tp)
print(type(tp))

# asignar el contenido de una tupla en diferentes variables
t = 1,2,3
x,y,z = t
print(x,y,z) # al tener la misma cantidad de valores que de variables, se asignan una a una, esto tambien funciona con listas y diccionarios

tx = 1,2,3,1
print(len(tx)) # imprime el largo de la tupla
print(t.count(1)) # Contar la cantidad de apariciones de un valor
print(t.index(2)) # consultar el indicie del valor