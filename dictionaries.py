diccionario = {
    "c1": "valor1",
    "c2": "valor2",
}  # Las claves no se pueden repetir, pero los valores si
print(diccionario)

resultado = diccionario["c1"]  # Buscar el valor de una clave
print(resultado)

cliente = {
    "nombre": "Karin",
    "apellido": "Tapian",
    "edad": 21,
    "peso": 40,
    "estatura": 12.5,
}

consulta = cliente["edad"]  # Pedir una consulta del dic cliente, en la clave edad
print(consulta)

# diccionario , lista dentro de un diccionario
# imprimir el valor de la clave 2, pero  el indicie 1 de este valor
dic = {"c1": 22, "c2": [10, 20, 40], "c3": {"s1": 100, "s2": 200}}
print(dic["c2"][1])  # 20

# Test

test = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
r = test["c2"][1]  # forma larga
print(r.upper())

print(test["c2"][1].upper())  # forma corta


# agregar elentos a un diccionario ya creado
diccionario_nuevo = {
    1: "A",
    2: "B",
    3: "C",
    4: 'D'
}
print(diccionario_nuevo)

diccionario_nuevo[5] = 'E' # Creas una clave que no existe y como esta se va a agregar, le das un valor
print(diccionario_nuevo)

# sobreescribir
diccionario_nuevo[2] = 'X' # invocas una clave del diccionario y le asignas otro valor
print(diccionario_nuevo)

# Conocer todas las claves de un diccionario
print(diccionario_nuevo.keys())

# Conocer los valores
print(diccionario_nuevo.values())

# todos los valores del diccionario
print(diccionario_nuevo.items())
# NOTA : el echo de que todo lo que nos mustra esta salida esta entre parentesis (), eso quiere decir que lo que esta dentro de los diccionarios es un tuples

# Guia -  https://claude.ai/public/artifacts/1550b6ba-0e0d-44f0-9307-cf207cc33b67