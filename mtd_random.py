# podes importar todos los metodos de una libreria con form random import *

from random import *

# random es un metodo que toca importar a python
# el nombre del archivo.py no deberia tener el nombre de la liberia a utilizar
# desde libreria importa metodo, para importar todo no se coloca el metodo si no un *
# from random import randint # si te da error, es que py necesita estar utilizando el metodo

numero = randint(1, 10)  # del 1 al 10 me dara un numero aleatorio
print(numero)

aleatorio = round(uniform(1, 5), 1)  # manda un decimal, tambien podes redondearlo
print(aleatorio)

aleatorio = (
    random()
)  # metodo vacio, elije un numero decimal entre 0 o 1, da una fraccion de un entero

colores = ["azul", "rojo", "amarillo", "verde", "negro"]
aleatorio = choice(colores)  # strings aleatorios
print(aleatorio)

# mesclar
numeros = list(range(5, 50, 5))
shuffle(
    numeros
)  # mescla aleatoria, no se puede utilizar con strings porque son inmutables
print(numeros)
