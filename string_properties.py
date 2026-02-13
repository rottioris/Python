# los strings en una variable no se pueden remplazar, la variables si se puedes sobreescribir.

a = "A"
print(a * 10)

t = """ Contrary to popular belief, Lorem Ipsum is not simply rando text.
It has roots in a piece of classical Latin literature from 45BC,
making it over 2000 years old. Richard McClintock"""

print(t)
print('popular' in t) # Esta en?
print('lorem' not in t) # No esta en?

print(len(t)) # ver el largo del texto en la variable