print ("-----    DIBUJAR UN TRIÁNGULO     -----")

filas = int(input("Introduce el número de filas: "))

# Generamos un patrón
for i in range(1, filas+1):
    print("*" *i)
for i in range(filas-1, 0, -1):
    print("*" *i)