# Zip lo que hace es unir dos listas
#   nombres = ['Eva','Juan']
#   edad = [22,12]
#   zip(nombres,edad)

nombres = ["Ana", "Valeria", "Miguel"]
edad = [23, 44, 56, 23]
ciudad = ["Lima", "Madrid", "Colombia"]
combinados = list(
    zip(nombres, edad, ciudad)
)  # para poder ver este nuevo objeto, toca castearlo dentro de una lista
print(combinados)

# Si agregas un elemento mas al cualquiera lista, este omite ese elemento, ya que zip solo llega hasta el largo de la lista mas corta

# # # # # #
# Crear un sistema que haga automaticamente la salida de cada objeto
for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} anios y vive en {ciudad}")
