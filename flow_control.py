# Palabras clave : If , Elif , Else
# Ejemplo:
# if una_condicion:
#     print(codigo_a)
# elif otra_condicion: # si no se cumple, cumple el siguiente
#     print(condicion_c)
# else:
#     print(codigo_b)

if 1 > 5:
    print('YES')


x = True

if x:
    print('True')

if 5 == 2: # Si esto no se cumple, py no imprime nada en pantalla
    print('YES!')
else: # Si la primera condicion no se cumple, pasa el else y imprime su contenido
    print('NO')

mascota = 'perro'

if mascota == 'gato': # Tienes un gato? Nop
    print("Gatoo!") # Paso
elif mascota == 'perro':  # Mascota es igual a perro? Si
    print('Tienes un perro') # Imprime  /// Si mascota no es igual a perro, este pasaria al else y imprimiria su contenido.
else:
    print('No se que animal tienes')

# Anidar if

edad = 12
nota = 9
if edad <17:
    print('No cumples la edad')
    if nota >= 5:
        print('Pasaste')
    else:
        print('No pasas')
else:
    print('Cumples la edad')
    