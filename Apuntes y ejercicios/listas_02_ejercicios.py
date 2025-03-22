
# ? Ejercicio 1: Recorrer una lista de nombres

# Dada la siguiente lista de nombres:

nombres = ["Ana", "Carlos", "Beatriz", "David", "Elena"]

# Escribe un programa que imprima cada nombre en una línea diferente.

for nombre in nombres:
    print(nombre)

# ? Ejercicio 2: Mostrar índices y valores

# Dada la siguiente lista:

colores = ["rojo", "verde", "azul", "amarillo"]

# Escribe un programa que muestre cada color junto con su posición en la lista.

for i, color in enumerate(colores):
    print(f"Índice {i}: {color}")

# Índice 0: rojo

# Índice 1: verde

# Índice 2: azul

# Índice 3: amarillo





# ? Ejercicio 3: Invertir el orden de una lista

# Dada la lista:

numeros = [10, 20, 30, 40, 50]

# Escribe un programa que imprima los números en orden inverso.

print(f"{numeros[::-1]}") # ! esta es la forma fácil sin modificarla
numeros.reverse()
print(numeros) # ! esta es la forma de darle la vuelta y después imprimirla sin más



# ? Ejercicio 4: Sumar los elementos de una lista

# Dada la lista de números:

valores = [3, 7, 2, 9, 1]

# Escribe un programa que calcule la suma total de los elementos de la lista y la muestre en pantalla.

suma_total = 0
for valor in valores:
    suma_total = suma_total + valor
print(f"La suma total de los valores dentro de la lista {valores} es de {suma_total}")



# ? Ejercicio 5: Filtrar números pares

# Dada la lista:

numeros = [12, 7, 5, 9, 16, 8, 3]


# Escribe un programa que genere una nueva lista con solo los números pares y la imprima.

for numero in numeros:  # ! con este bucle muestro los valores pero no los estoy asignando a una nueva lista
    if numero % 2 == 0:
        print(numero, end=" ")
print()

numeros_pares = [] # ? inicializo la lista vacía para poder usarla dentro del bucle
for numero in numeros:  # ! ahora sí los estoy añadiendo a una nueva lista
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(numeros_pares)



# ? Ejercicio 6: Encontrar el número más grande

# Dada la lista:

edades = [15, 22, 30, 18, 27, 35, 10]

# Escribe un programa que encuentre y muestre el número más grande de la lista, sin utilizar métodos

mayor = 0  # ! una vez más juego con una variable temporal que modificaré cada vez que un número sea mayor para guardarlo
for edad in edades:
    if edad > mayor:
        mayor=edad
print(f"El número {mayor} es el mayor de la lista: {edades}.")




# ? Ejercicio 7: Contar cuántas veces aparece un elemento

# Dada la lista:

letras = ["a", "b", "c", "a", "d", "b", "a", "c"]

# Escribe un programa que pregunte al usuario una letra y luego muestre cuántas veces aparece en la lista

# Utiliza el método count()

letra_a_buscar = input(f"¿Qué letra deseas buscar en esta lista: {letras}? ")

cantidad = letras.count(letra_a_buscar) # ! este método me debería devolver un int con el número de veces que sale el elemento entre paréntesis dentro de la lista de antes del .count
if cantidad == 0:
    print(f"La letra {letra_a_buscar} no se encuentra en la lista {letras}.")
elif cantidad == 1:
    print(f"La letra {letra_a_buscar} se encuentra {cantidad} vez en la lista {letras}.")
else:
    print(f"La letra {letra_a_buscar} se encuentra {cantidad} veces en la lista {letras}.")