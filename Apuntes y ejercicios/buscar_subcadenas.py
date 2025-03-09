# Buscar subcadenas

cadena = "Hola Mundo!"

indice = cadena.find("Mundo")
print (f"Índice de la cadena Mundo: {indice}") # Me dice la posición de la cadena donde está lo que he buscado
indice = cadena.find("mundo")
print (f"Índice de la cadena Mundo: {indice}") # Si no encuentra nada te da un -1, ya que la función es case sensitive
indice = cadena.find("o")
print (f"Índice de la cadena Mundo: {indice}") # Solo muestra la posición de la primera vez que lo encuentra