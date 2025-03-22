
# ! ------------- LISTAS -------------

lista = [1,2,3,4,5]

# Imprimir lista
print(f"Lista original: {lista}")
print(f"El tipo de dato de la lista es: {type(lista)}")

# Longitud de la lista
print(f"La longitud de la lista (el número de elementos que contiene) es: {len(lista)}")

# Acceder a los elementos de la lista
print(f"El primer elemento de la lista es: {lista[0]}")

# Acceder al último elemento de la lista
print(f"El último elemento de la lista es: {lista[len(lista)-1]}") # ! El último elemento es el del valor de la longitud de la misma -1, ya que empezamos desde el 0
print(f"El último elemento de la lista es: {lista[-1]}")

# Invertir los elementos de una lista
# print(lista.reverse()) # ! ESTO ES INCORRECTO, PRIMERO HAY QUE INVERTIR Y LUEGO MOSTRAR, YA QUE SINO DEVUELVE NONE
lista.reverse()
print(f"Lista invertida: {lista}")

print(f"{lista} --> Lista original")
print(f"{lista[::-1]} --> Lista invertida") # Las listas funcionan como strings, puedo invertirlas de la misma forma

# Recorrer una lista mediante 'for'

print("Listado de los elementos de la lista: ", end=" ")
for valor in lista:
    print (valor, end=" ")
print()

# Comprobar si un valor está en la lista (en este caso el 4)

if 4 in lista:
    print ("El nº 4 está en la lista.")
else:
    print ("El nº 4 no está en la lista.")

# Otra forma de recorrer una lista
frutas = ["manzana", "pera", "plátano", "uva"]

for i in range(len(frutas)): # ! Esto es exactamente lo mismo que for i in frutas
    print(f"Índice {i}: {frutas[i]}")  # ? HAY UN MÉTODO AUTOMATIZADO PARA ESTO LLAMADO ENUMERATE

# ! Método enumerate

for i, fruta in enumerate(frutas):
    print (f"Índice {i}: {fruta}")

# ! de forma inversa

for fruta in reversed(frutas):
    print(fruta, end=" ") 
print()


for fruta in frutas[::-1]:
    print(fruta, end=" ")
print()

# Con el método while (utilizamos j porque i vale 3 por el bucle anterior)
j = 0
while j < len(frutas):
    print(frutas[j])
    j += 1

