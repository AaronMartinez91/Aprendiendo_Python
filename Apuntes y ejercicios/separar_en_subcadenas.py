# Separar en subcadenas

datos = "Estáis aburridos? Verdad que no?"
lista = datos.split() # El método split separa por defecto, cada elemento POR ESPACIOS
print(f"Datos por espacios con split: {lista}")

usuario = "Ester Colero, 50, L'Hospitalet"

print(f"Separo mediante lo que defino, en este caso las comas: {usuario.split(",")[0]}")

