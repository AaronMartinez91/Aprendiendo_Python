"""
La empresa que opera en internet: niUnDuro.com  Nos ha contratado porque necesita un programa en Python que: dados una serie de datos que introduce el cliente, calcule el interés compuesto

El interés compuesto se calcula con la siguiente fórmula:

﻿A igual P multiplicación en cruz paréntesis izquierdo 1 más r normal dividido por n paréntesis derecho elevado a n multiplicación en cruz t fin elevado﻿


Donde:

A → Monto final después de los intereses (dinero final que tendrás).
P → Capital inicial o inversión inicial.
r → Tasa de interés anual en decimal (por ejemplo, 5% = 0.05).
n → Número de veces que se capitaliza el interés al año.
t → Número de años.


Requisitos del programa:
Pedir al usuario los siguientes datos de entrada:
Capital inicial (P)
Tasa de interés anual en porcentaje (r)
Número de veces que se capitaliza el interés por año (n)
Número de años (t)


Se pide:  realizar un programa en Python que nos permita:

Calcular el monto final (A) usando la fórmula del interés compuesto.
Mostrar el resultado formateado a 2 decimales.
"""

try: # una vez tengo el programa, aplico control de datos para asegurarme de que no se rompa
    # En primer lugar necesito pedir los datos al cliente y almacenarlos en variables para poder operar con ellos
    p = float(input("Por favor, introduzca el capital inicial: "))
    r_porcentaje = float(input("Por favor, introduzca el porcentaje de la tasa de interés anual: "))
    # como le pedimos un interés a nivel porcentual pero necesitamos un decimal para operar con él, lo cambiamos:
    r = r_porcentaje/100
    n = int(input("Por favor, introduzca el número de veces que se capitaliza el interés por año: "))
    t = int(input("Por favor, indique el número de años: "))


    # Aplicamos la fórmula, en este caso prefiero usar el nombre de la variable en lugar de A para tenerlo más claro
    interes_compuesto = p * (1 + r/n)**(n*t)

    # Mostramos el resultado en pantalla con dos decimales:
    print(f"El interés compuesto de {p:.2f}€ a un interés del {r_porcentaje:.2f}%, con un total de {n} capitalizaciones anuales, en un total de {t} años corresponde a {interes_compuesto:.2f}€.") 
except ValueError:
    print("Por favor, empiece desde el principio asegurándose de que los datos introducidos son correctos.")