# Puedo asignar de forma múltiple valores a variables
x, y, z = 5, "Hola", 4.9

print(f"x = {x}, y = {y}, z = {z}")

# Dado dos variables a,b. Se pide intercambiar su contenido utilizando asignación múltiple

a = 5
b = 10

a, b = b, a
# si ponemos a = b, y luego b = a, ya hemos reasignado el valor de "a" y por tanto tendremos dos valores iguales, al hacerlo de forma múltiple esto no pasa

print(f"a = {a}, b = {b}")