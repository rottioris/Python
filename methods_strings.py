# Metodos
# upper () - pasar a MAYUS
# lower () - pasar a minus
# slipt () - separado en partes (lista)
# join  () - unir items usando un separador
# find  () - encontrar un sub-string
# replace () - reemplazar un sub-string

text = "Este es un texto de prueba"
r_upper = text[5].upper()
r_lower = text.lower()
r_slipt = text.split('t') # t se toma como el separador
r_find = text.find('s') # busca un determinado caracter, si no encuentra nada devuelve -1
r_replace = text.replace('texto','todos') # remplaza el primer argumento, por el segundo, tambien puedes reemplazar una letra por otra en todo el texto

print(r_upper)
print(r_lower)
print(r_slipt)
print(r_find)
print(r_replace)

# Join

a = "Hola"
b = "esto"
c = "es"
d = "join"
e = " ".join([a,b,c,d]) # la separacion puede ser cualquier cosa
print(e)