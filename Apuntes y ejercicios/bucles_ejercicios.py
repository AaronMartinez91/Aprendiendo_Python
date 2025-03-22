from random import randint

# Ejercicio 1.- Esribe un programa que imprima los números del 1 al 10 utlizando un bucle for.
# El resultado tiene que salir en UNA SOLA LÍNEA

for i in range (1,11):
    print(i, end=" ")
print()

# Ejercicio 2.- Escribe un programa que imprima los números del 1 al 7 utilizando un bucle while.
# El resultado tiene que salir en UNA SOLA LÍNEA

num = 1
while num < 8:
    print(num, end=" ")
    num += 1
print()

# Ejercicio 3.- Haz un programa que pida al usuario que introduzca números. El programa los sumará hasta que introduzca un cero. Después mostrará la SUMA TOTAL

suma_total = 0
control = True
while control:
    try:
        num2 = float(input("Introduzca un número: "))
        if num2 == 0:
            control = False
        else: 
            suma_total = suma_total + num2
    except ValueError:
        print("Debes introducir un número para poder operar con él.")       
print(f"La suma total de los valores introducidos es: {suma_total}.")


# Ejercicio 4.- Escribe un programa que imprima sólo los números impares del 3 al 15

# for j in range (3,16,2):
#     print(j)


# for j in range (3,16,):
#     if j % 2 != 0:
#         print(f"{i}", end=" ")


for j in range (3,16,):
    if j % 2 == 0:
        continue
    print(f"{j}", end=" ")



# Ejercicio 5.- Escribe un programa que pida un número y muestre la tabla de multiplicar de ese número hasta el 10

while True:
    try:
        num3 = float(input("Introduce un número para ver su tabla de multiplicar: "))
        for k in range (1,11):
            print(f"{num3} * {k} = {num3*k}", end="\t\t")
        print()
        break    
    except ValueError:
        print("Debes introducir un número para poder hacer su tabla de multiplicar.")

# Ejercicio 6.- Realiza un programa que genere un número aleatorio entre 1 y 10. El usuario tiene que adivinarlo

aleatorio = randint(1,10)
print("Se ha generado un número aleatorio del 1 al 10.")
while True:
    try:
        intento = int(input("Introduce un número a ver si lo adivinas: "))
        if intento == aleatorio:
            print(f"¡Enhorabuena! Has acertado, el número era: {aleatorio}")
            break
        elif intento < 1 or intento > 10:
            print(f"El número {intento} no es número entre el 1 y el 10.")
        else:
            print(f"El número {intento} no es correcto, vuelve a intentarlo.")
    except ValueError:
        print("Debes introducir un número entero entre el 1 y el 10.")

# Ejercicio 7.- Realiza un programa que genere un número aleatorio entre el 1 y 10. El usuario tiene que adivinarlo, sólo disondrá de 5 intentos. Este valor lo guardaremos en una CONSTANTE llamada vidas. Cada vez que el usuario introduzca un número, el programa le dirá si el número secreto es mayor o menor. Si el usuario acierta, gana el juego. Si se queda sin intentos, pierde y el programa revelará el número secreto.

VIDAS = 5
aleatorio2 = randint(1,10)
contador_vidas = 0
print("Se ha generado un número aleatorio del 1 al 10. Tienes 5 intentos para adivinarlo: ")
while VIDAS - contador_vidas > 0:
    try:
        intento2 = int(input("Introduce un número a ver si lo adivinas: "))
        contador_vidas += 1
        if intento2 == aleatorio2:
            print(f"¡Enhorabuena! Has acertado, el número era: {aleatorio2}")
            break
        elif intento2 < 1 or intento2 > 10:
                print(f"El número {intento2} no es número entre el 1 y el 10.")
        else:
            if intento2 < aleatorio2:
                print(f"El número secreto es mayor que {intento2}, vuelve a intentarlo.")
            else:
                print(f"El número secreto es menor que {intento2}, vuelve a intentarlo.")

    except ValueError:
        print("Debes introducir un número entero entre el 1 y el 10.")
        contador_vidas += 1 # Aquí controlo que le cueste un intento incluso cuando no pone un número
if VIDAS == contador_vidas:
    print(f"Lástima, te has quedado sin vidas... El número secreto era {aleatorio2}.")
