
# ! ------------matrices------------
matriz = [[10,2,3], [4,50,900], [7,800,10]] # Definimos una matriz 3 x 3

# para imprimirla:

for fila in matriz:
    print (fila)

# imprimimos utilizandola función format

for fila in matriz:
    print("{:5d} {:5d} {:5d}".format(*fila))       # ? reserva 5 espacios para imprimir el dígito. El * hace de puntero hacia el valor de la fila

print(f"Elemento en la segunda fila y tercera columna: {matriz[1][2]}")
