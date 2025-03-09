# Convertir cadenas a números

no_cadena = '10'
# print(f"1.-Le sumo una unidad a {no_cadena} = {no_cadena+1}") ERROR, ya que no le puedo sumar un número a una cadena
print(f"2.-Le sumo una unidad a {no_cadena} = {no_cadena}+1") # aquí concateno, no sumo 
print(f"3.-Le sumo una unidad a {no_cadena} = {int(no_cadena)}+1") # debo convertir a formato int, aquí concatena porque el +1 es str
print(f"4.-Le sumo una unidad a {no_cadena} = {int(no_cadena)+1}") # debo convertir a formato int, aquí suma porque el 1 es int


# Pedir al usuario un número y que me devuelve el doble de ese número

numero = float(input("Introduce un número: ")) # lo convertimos a float, ya que queremos operar con él

print(f"El doble de {numero:.2f} es: {numero*2:.2f}.")