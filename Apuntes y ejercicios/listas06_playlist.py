
#! ---------------------- PLAYLIST -----------------------

# Creamos una lista vacía

lista_reproduccion = []

numero_canciones = int(input("¿Cuántas canciones deseas agregar?: "))

for indice in range (numero_canciones):
    cancion = input(f"Proporciona la canción {indice+1}: ")
    # lista_reproduccion += cancion #? mejor usar el método que concatenar
    lista_reproduccion.append(cancion) 

# ordenar la lista según orden alfabético
lista_reproduccion.sort() # ? importante recordar que no podemos meter esto directamente en un print, devolverá None. Hay que hacerlo en dos líneas
                          #! en el caso de los símbolos o letras, .sort() ordena por tabla ascii, por tanto primero ordena mayúsculas 
# Mostrar la lista

for cancion in lista_reproduccion:
    print(f"-{cancion}.")

