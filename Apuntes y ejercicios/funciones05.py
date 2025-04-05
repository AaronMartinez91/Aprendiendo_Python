
#! Ejercicio 1:
x = 10
def imprimir_x():
    print(x)       #? puedo acceder PARA LEER la variable global

imprimir_x()  #! importante! esto SÍ funciona, ya que el global es necesario para MODIFICAR la variable, no para leerla

#! Ejercicio 2:
z = 99

def imprimir_z():
    z=5             #? variable local, aunque se llame igual es OTRA
    print(z)

imprimir_z()  #? por ello imprime aquí 5
print(z)      #? y aquí 99

#! Ejercicio 3: MODIFICAR UNA VARIABLE GLOBAL(NO)
y= 20
def modificar_y():
    y=30
    print(f"y dentro de la función: {y}")

modificar_y()
print(f"y fuera de la función {y}")

#! Ejercicio 4:
w = 40
def modificar_w():
    global w            #? modifico directamente la variable GLOBAL por lo que ambos resultados muestran lo mismo
    w += 1
    print(f"w dentro de la función, {w}")

modificar_w()
print(f"w fuera de la función, {w}")

