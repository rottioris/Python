# Conversion between types

integer = 1
number = int(integer) # Conversion Explicita
print(number)
print(type(number))

num1 = 20
num2 = 30.5

num1 = num1 + num2 # Conversion implicita


edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
nueva_edad = 1 + edad
# print("Tu nueva edad es: " + nueva_edad) TypeError: can only concatenate str (not "int") to str
print(type(edad))