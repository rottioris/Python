name = input("Digite su nombre: ")
sell = input("Cuanto ha vendido: ")

comision= int(sell) * 13 / 100

print(f"Su nombre es {name} y su comision es del {round(comision,2)}")
