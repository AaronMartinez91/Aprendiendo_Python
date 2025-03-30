
# ! Eliminar elementos de una lista

lista = [1,2,3,4,5,6,7,8,9,10]

print(f"{lista} -> Lista original")

# Eliminar UN SOLO elemento de la una lista: MÉTODO .remove(), SOLO ELIMINA EL PRIMER ELEMENTO

# ! al igual que el reverse, tengo que hacerlo a parte, no puedo hacerlo todo en una misma línea
lista.remove(7) # ? si pongo un valor que no está en la lista se rompe
print(f"{lista} -> eliminando el elemento entre paréntesis con el .remove(7)")

# ! print(lista.remove(2)) --> NONE, NO SE PUEDE

# Eliminamos por ÍNDICE con el método pop(), no puedo hacerlo seguido tampoco
lista.pop(1) # ? elimino el elemento de la posición [1]
print (f"{lista} -> eliminando el índice [1] con la función .pop(1)")

# Elimino utilizando otro método: 'del', también elimino ÍNDICES
del lista[7] # ? elimino el elemento de la posición [7]
print (f"{lista} -> eliminando el índice [7] con la función 'del' ")

# Utilizando slicing
del lista[5:]
print (f"{lista} -> eliminando desde el índice [5] hasta el final con la función 'del' ")

# Obtener sublistas
sublista = lista[2:4] # genera una sublista del índice

print(f"sublista [2:4]: {sublista}")

