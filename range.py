# apelar a un rango, tambien se puede poner (1,5) para que inicie desde el 1 y no desde el 0
for numero in range(5):
    print(numero)

# tambien puedes incluir un tercer parametro, los pasos que va a dar al contar

for numero2 in range(20, 50, 2):
    print(numero2)

# range tambien se puede utilziar por fuera de los loops
# como crear una lista del 1 al 1000

lista = list(
    range(1, 1001)
)  # 1001? para poder incluir al 1000, ya que no cuenta el ultimo numero
