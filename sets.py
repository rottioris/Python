# 1) Formas de declarar un set
# - Usando la palabra clave `set()` con UN solo argumento iterable:
#   set([1, 2, 3])
#   set((1, 2, 3))
#   set({1, 2, 3})
#
# - Usando llaves directamente (sin `set`):
#   {1, 2, 3}
#
# Nota:
# Aunque las llaves también se usan para diccionarios, Python reconoce
# un set porque no contiene pares clave:valor.

# 2) Restricciones de `set()`
# - `set()` solo acepta un argumento.
# - Ese argumento debe ser iterable (lista, tupla, set, etc.).
# - NO es válido: set(1, 2, 3)

# 3) Características de los sets
# - Solo admiten elementos únicos (los duplicados se eliminan).
# - No están ordenados.
# - No se pueden indexar (no existe set[0]).
# - Son mutables (se pueden agregar o eliminar elementos),
#   pero sus elementos deben ser inmutables.

# 4) Tipos de datos permitidos en un set
# - Permitidos: int, float, str, tuple (inmutable).
# - NO permitidos: list, dict, set (porque son mutables).


mi_set = set([1,2,3,4,5,4,4,2,1]) # recordar cuando se utiliza set() debes colcoar los valores entre un conjunto de llaves
print(type(mi_set))
print(mi_set)

# si se admiten tuples
set_set = set([1,2,3,4,(1,2,3,),1,1,1])
print(set_set)

# funciones
set1 = set((1,2,3,4,5,6))
print(len(set1)) # ver el largo de una coleccion
print(2 in set1) # consulta (true or flase) # tambien se puede hacer con tuples, listas o diccionarios si buscas las claves


# union de sets
s1 = {1,2,3}
s2 = {3,4,5} # recordad que set no repite elementos
s3 = s1.union(s2)
print(s3)

# metodo agregar
st1 = {1,2,3,4}
st1.add(5)
print(st1)

# eliminar
st1.remove(2)
print(st1)

# descartar
st1.discard(6) # funciona igual que remove pero no da error si descarta un elemento que no existe
print(st1)

# pop
st1.pop() #elemina un elemento aleatorio, ya que los sets no tienen un orden
print(st1)

ss = {1,2,3,4,5}
sorteo = ss.pop()
print(sorteo)

# limpiar el set
ss.clear()
print(ss)