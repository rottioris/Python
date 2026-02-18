# Minimo y Maximo, sirve para dectectar valores altos y bajos

minimo = min(2, 42, 14, 23, 11)
print(minimo)  # 2

maximo = max(2, 42, 14, 23, 11)
print(maximo)  # 42

# trabajar con una lista

lista = [21, 2, 4, 43, 151]
print(max(lista))
# con una cadena literal
print(f"max {max(lista)} / min {min(lista)}")

# trabajar con strings
# ordenables alfabeticamente

nombres = ["juan", "carlos", "alicia"]
print(min(nombres))

# si trabajas con un solo string
# busca primero en mayusculas y luego minusculas

nombre = "Francisco"
print(
    min(nombre.lower())
)  # Si quieres hacer que busque sin importar las mayusculas, tenes el metodo lower, si lo quitas imprimira F como la letra minima

# con diccionarios

dic = {"c1": 44, "c2": 11}
print(
    min(dic)
)  # imprime por defecto la clave que tiene el valor mas inferior, si quiero el valor min, podes pedir el valor con values # C1
print(min(dic.values())) # 11
