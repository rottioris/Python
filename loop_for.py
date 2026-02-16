# nombres = ['Juan','Guille','Liz']
# Como seria?
# Por cada elemento en nombres # 'Cada elemento' hace referencia a los items de la lista, asi que esta variable contrendria el elemento en cada iteracion, cuando imprime hola juan, esa variable obtiene el elemento juan
#       imprimir ("hola")
# for in nombres:
#       print("hola")


lista = ["a", "b", "c"]  # objeto iterable
for letras in lista:
    numero_letra = (
        lista.index(letras) + 1
    )  # por cada letra muestra su index # este comienza a contar desde cero, se suma un uno, para que sea 1 2 3, en vez de 0 1 2
    print(f"letra {numero_letra}: {letras}")


nombres = ["juan", "samuel", "guille", "pedro", "sara"]  # objeto iterable
for elemento in nombres:
    # checkear si comienza con un caracter
    if elemento.startswith("s"):
        print(elemento)
    else:
        print("No comienzan con L")


numeros = [1, 2, 3, 4, 5]
valor = 0  # en cada vuelta suma un numero de la lista +1 + 2 +3 +4 +5

for numero in numeros:
    valor = valor + numero
print(
    valor
)  # print al estar al mismo nivel que el for solo se ejecuta cuando el loop finaliza


palabra = "python"
# no hace falta colocar la variable afuera, en vez de palabra podria ser el contenido de la variable y se imprimiria de la misma manera
# for letra in 'python', tambien podria ser una lista o una tupla, tambien iterar en un tuple o una lista que tenga lista
for letra in palabra:
    print(letra)

for nmro in [[1, 2], [2, 4], [3, 5]]:
    print(nmro)

# tambien podes imprimir los objetos de cada lista por separado
# a seria el primer elemento de la lista y b el segundo elemento de la lista, esto para cada sublista
for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

# iterar en un diccionario

dic = {"c1": "a", "c2": "b", "c3": "c"}
for item in dic.items(): #imprimir todo completo, si es valores es values()
    print(item)
