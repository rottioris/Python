# Comparaciones
# 4 < 5
# 5 < 6

mi_bool = (4 < 5) and (5 > 6) # False >> para que se de verdadero se tienen que cumplir los 2 valores a la vez.
print(mi_bool)

mi_bool = (5 == 5) and ('cat' == 'cat') # No importa que se este comparando


mi_bool = 10 == 20 or 3 == 3 # 10 es igual a 20? falso, pasa a la siguiente 3 == 3? Verdadero, mientras una de las 2 comparaciones se cumpla, mostrara verdadero.

texto = 'Esta frase es breve'
mi_bool = ('es' in texto) and ('Esta' in texto)


mi_bool = not 'a' != 'a' # Si no es verdad | doble negacion