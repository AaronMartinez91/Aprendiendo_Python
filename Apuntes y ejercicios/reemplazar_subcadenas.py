# Reemplazar subcadenas

cadena = "Hola, mundo!"
print(f"1.- Cadena original: {cadena}")

nueva_cadena = cadena.replace("mundo", "a todos")
print(f"1.- Nueva cadena reemplazada: {nueva_cadena}") # al igual que el find, solo cambia lo primero
nueva_cadena = cadena.replace("Mundo", "a todos")
print(f"1.- Nueva cadena reemplazada: {nueva_cadena}") # si no existe lo que busco no cambia nada