# Ejercicio: contar el número total de dígitos que tiene un número

# Por ejemplo, el número 75893, tendría 5 dígitos

# controlador_bucle = True
# while controlador_bucle:
#     try:
#         original = num = int(input("Por favor, introduce un número para saber el total de dígitos que tiene: "))
#         count = 0
#         while num != 0:
#             num = num // 10
#             count += 1

#         print(f"El número {original} tiene {count} dígitos") 
#         controlador_bucle = False
#     except ValueError:
#         print("Debes introducir un número entero.")


# Bien hecho, con una función:
def contador_num(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1

    print(f"El número {original} tiene {count} dígitos")
    return 

try:
    original = num = int(input("Por favor, introduce un número para saber el total de dígitos que tiene: "))
    contador_num(num)
except ValueError:
    print("Debes introducir un número entero.")