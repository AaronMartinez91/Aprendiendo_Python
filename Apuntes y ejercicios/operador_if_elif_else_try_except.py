""" 
Pedir la edad al usuario, 
si la edad es menos que 0: saldrá un error diciendo que la edad no puede ser negativa.
si la edad es menor o igual a 12. Nos dirá que eres un niño
si la edad es menor o igual a 17. Saldrá que es un adolescente
si la edad es menor o igual a 30 eres un joven adulto
si la edad es menor o igual a 64 eres un adulto
en caso contrario, todavía estás vivo???
"""

try:

    edad = int(input("Por favor, introduce tu edad en años: "))
    if edad < 0:
        print("La edad no puede ser negativa.")
    elif edad <= 12:
        print("Eres un crío.")
    elif edad <= 17:
        print("Eres un adolescente, deja ya las pajas.")
    elif edad <= 30:
        print("Eres un joven adulto.")
    elif edad <= 64:
        print("Eres un adulto.")
    else:
        print("Es hora de tu medicación.")

except ValueError: # Es muy importante en el except poner el tipo de error que da el IDE
    print("❌ Error. Debes introducir un número válido.")        