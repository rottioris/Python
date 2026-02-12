texto = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'

resultado = texto[0] # Indice
resultado = texto.index("is") #Busqueda de palabras o letras
resultado = texto.index("s",6, 10) # -->
resultado = texto.rindex("u",3) # <--
print(resultado)