"""
Ejercicio:
Escribe un programa en Python que genere 1000 números aleatorios. Cada número debe ser 0 o 1.
El programa nos tiene que decir cuántas veces aparece el número 0 y cuántas el número 1.
Muestra el resultado al final del programa indicando:
    Número de veces que ha salido el cero.
    Número de veces que ha salido el uno.
    Crear la constante N_veces = 1000
    Añadir el porcentaje de cada una.
"""

from random import randint
N_VECES = 500000
numeros0 = 0
numeros1 = 0

for i in range (N_VECES):
    aleatorio = randint(0,1)
    if aleatorio == 0:
        numeros0 += 1
    else:
        numeros1 += 1

print(f"Sobre un total de {N_VECES}, la cantidad de veces que ha salido 0 es: {numeros0} ({numeros0*100/N_VECES}%) y la cantidad de veces que ha salido 1 es {numeros1} ({numeros1*100/N_VECES}%).")    
