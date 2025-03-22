# Nuestro PIN secreto 2935
pin_secreto = "2935"

# Bucle anidado para probar todas las combinaciones posible de 4 dígitos
for d1 in range (10): # para el primer dígito
    for d2 in range (10):
        for d3 in range (10):
            for d4 in range (10):
                intento = f"{d1}{d2}{d3}{d4}"
                if intento == pin_secreto:
                    print(f"El pin secreto es {intento}")
                    break # Este break solo para la iteración interna
print(intento)

# Cerramos todos los bucles al cumplir la condición
for d1 in range (10): 
    for d2 in range (10):
        for d3 in range (10):
            for d4 in range (10):
                intento = f"{d1}{d2}{d3}{d4}"
                if intento == pin_secreto:
                    print(f"El pin secreto es {intento}")
                    break
            if intento == pin_secreto:
                break   
        if intento == pin_secreto:
            break 
    if intento == pin_secreto:
        break          
print(intento)

# Podemos forzar una excepción
try:
    for d1 in range(10):  
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    intento = f"{d1}{d2}{d3}{d4}"
                    if intento == pin_secreto:
                        print(f"El pin secreto es {intento}")
                        raise StopIteration  # Lanzamos una excepción para salir
except StopIteration:
    pass  
print(intento)


# Variable de control para salir de los bucles
encontrado = False

for d1 in range(10):  
    for d2 in range(10):
        for d3 in range(10):
            for d4 in range(10):
                intento = f"{d1}{d2}{d3}{d4}"
                if intento == pin_secreto:
                    print(f"El pin secreto es {intento}")
                    encontrado = True
                    break  # Sale del cuarto bucle
            if encontrado:
                break  # Sale del tercer bucle
        if encontrado:
            break  # Sale del segundo bucle
    if encontrado:
        break  # Sale del primer bucle
print(intento)


# Por último, la forma más correcta sería con una función que devuelva el valor
def encontrar_pin():
    for d1 in range(10): 
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    intento = f"{d1}{d2}{d3}{d4}"
                    if intento == pin_secreto:
                        print(f"El pin secreto es {intento}")
                        return  

encontrar_pin()