
#! ------------------------------ EJEMPLO TUPLAS -------------------------------

mi_tupla = (1,2,3,4)
print("Tupla: ", mi_tupla)

# Una tupla es una estructura ordenada de datos en Python que permite una colección ordenada e INMUTABLE

# Acceder a un elemento de la tupla:
print(f"Accedo al primer elemento de la tupla: {mi_tupla[0]}") # ? aunque la tupla se defina con (), cuando accedemos a una posición de la misma seguimos usando []

#! mi_tupla[0] = 99  INMUTABLE
#! print(mi_tupla)

print(type(mi_tupla))

# Desempaquetar una tupla:
a,b,c,d = mi_tupla

print(f"Desempaqueto tupla: {a} {b} {c} {d}")
a += 1
print(a) #? puedo trastear la variable a, porque es una variable independiente de la tupla.

# Concatenar tuplas:
tupla1 = (1,2,3)
tupla2 = (4,8,16)
print(f"Concatenación: {tupla1} + {tupla2} = {tupla1+tupla2}")

# Cálculo de la longitud de una tupla:
print(f"La longitud de la tupla {tupla1} es: {len(tupla1)}")

# Contar ocurrencias de un elemento en una tupla (igual que en los arrays)
tupla3 = (1,2,3,3,3,34,3)
print(f"Ocurrencias del nº 3 en {tupla3}: {tupla3.count(3)}")

mi_lista = [10,20,30] # lista
mi_tupla_desde_lista = tuple(mi_lista) # Creo una tupla desde una lista sin tocar la lista original
mi_lista_desde_tupla = list(mi_tupla_desde_lista) # Creo una lista desde una tupla

# Recorrer una tupla:
mi_tupla = ("rojo", "naranja", "verde")
for color in mi_tupla:
    print(color, end=" ")
print()    

# Comparación tuplas con listas
"""
CARACTERÍSTICA                                      TUPLA                                       LISTA

Mutabilidad                                         Inmutable                                   Mutable

Sintaxis                                            (elemento1, elemento2)                      [elemento1, elemento2]

Rendimiento                                         Rápida(inmutable)                           Lenta(mutable)

¿Cuándo usar?                                       Datos fijos                                 Datos dinámicos
"""