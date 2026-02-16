# while = mientras que una condicion se cumpla
# white una_condicion:
#   #un_codigo
# else tambien se puede agregar

moneda = 10
# condicion para que el bucle while se repita
while moneda > 0 :
        print(f'moneda {moneda}')
        moneda -= 1 #  linea encargada de hacer que el loop finalice para que no se ejecute infinitamente el loop
else:
    print('Sin monedas')


# no esta predeterminado cuantas veces se va a ejecutar, si no que depende de la dinamica del codigo
respuesta = 's'
while respuesta == 's':
    respuesta = input('continuar? S/N: ')
else:
    print('gracias')

# palabras clave para loops, while y for

# pass = pasar del lopp
solucion = 's'
while solucion == 's':
    pass

# break = interrumpir y salir del loop
nombre = input('nombre: ')
for letra in nombre:
    if letra == 'r': # al encontrarse el loop con la letra 'r' este finaliza por el break
        break
    print(letra)

# continue = continuar, interrumpe la operacion pero no el loop, si no que regresa con la siguiente iteracion

for letra in nombre:
    if letra == 'r':
        continue # saltara la 'r'
    print(letra)