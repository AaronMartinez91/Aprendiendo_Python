# Manejo de subcadenas (string)
cadena = "Hola_Mundo!"

# Obtenemos la subcadena [inicio:fin(SIN INCLUIR)]

subcadena1 = cadena[0:4]
print (subcadena1)

subcadena2 = cadena[5:12]
print (f"Segunda subcadena: {subcadena2}")

# Obtener una subcadena DESDE EL PRINCIPIO, si vamos a empezar por el principio, podemos poner el 0 o no poner nada (sin crear una variable extra, no es necesario pero se puede hacer)

print(f"Subcadena desde el principio: {cadena[:5]}")

# Obtener una subcadena DESDE EL FINAL, el mismo concepto, si no pongo límite, establece automáticamente el final de la cadena, este sí que incluye el último número

print(f"Subcadena desde el final: {cadena[5:]}")

# Con índices negativos, empiezas a contar desde la derecha en lugar de la izquierda

print (f"Subcadena contando desde la derecha: {cadena[-9:-1]}")
