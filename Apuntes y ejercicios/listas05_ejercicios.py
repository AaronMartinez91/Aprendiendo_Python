from random import randint

# ? Ejercicio 1: 
# ? Realizar un programa que inicialize una lista con 10 valores aleatorios(del 1 al 10) y posteriormente muestre por pantalla cada elemento de la lista junto con su cuadrado y su cubo


numeros = [randint(1,10) for _ in range(10)]
print(numeros)

for n in numeros:
    print (f"Número: {n:3}  | cuadrado: {n**2:4}  | cubo: {n**3:4}")


# ? Ejercicio 2
# ? Dada la siguiente lista 'numeros', crear una segunda lista con los cuadrados de la anterior

numeros = [1,2,3,4,5]
cuadrados = []
for n in numeros:
    cuadrados.append(n**2)
print(cuadrados)

# ? Ejercicio 3
numeros = range(10+1)
pares = [x for x in numeros if x % 2 == 0]
print(pares)