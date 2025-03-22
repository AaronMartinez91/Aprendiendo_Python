"""
            BUCLES O ITERACIONES
            range(start, stop, step)
            start --> valor inicial (opcional, por defecto 0)
            stop --> valor final (NO INCLUDE)
            step --> incremento o decremento (saltos, opcional, pordefecto vale 1)
"""

print("\n A.-")
for x in range(9): # el 9 no está incluido, es el 'stop'
    print(f"{x}", end=" ") # el end quiere decir que en cada finalización aplique un espacio en lugar de un salto de línea

print("\n B.-")
for x in range (1,5): # no saldrá 0, porque empezamos por el 1 y terminamos en 4 (5 sin incluir)
    print(f"{x}", end=" ")

print("\n C.-")
for x in range (1,11,2): # saltando de 2 en 2, una vez más el 11 no está incluido
    print(f"{x}", end=" ")

print("\n D.-")
for x in range (-5,6,2): # en negativo pero saltando en positivo
    print(f"{x}", end=" ")    

print("\n E.-")
for x in range (11,-11,-2): # del revés
    print(f"{x}", end=" ")

print("\n F.-")
frutas=["Manzana", "Plátano", "Pera"]
for i in range (len(frutas)): # saltamos hasta la longitud de la lista
    print(f"{i} {frutas[i]}") # imprimimos primero el valor del iterador y luego el contenido de la lista en la posición con valor del iterador