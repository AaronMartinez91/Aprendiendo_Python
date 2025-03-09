import datetime # fecha y hora actual
import random   # nº aleatorio


# Mostrar menú
print("Menú de opciones: ")
print("\t 1️⃣ - Saludar")
print("\t 2️⃣ - Mostrar fecha y hora actual")
print("\t 3️⃣ - Mostrar un número aleatorio")
print("\t 4️⃣ - Salir")

# Pedir al usuario una opción: 
try:
    opcion = int(input("Selecciona una opción [1-4]: "))
    match opcion:
        case 1:
            print("Hola que tal")
        case 2:
            # print(f"{datetime.datetime.now()}")
            # el formato datetime es bastante terrible y muestra hasta los milisegundos, así que lo formateamos para verlo mejor (consular en w3schools)
            print(f"{datetime.datetime.now().strftime("%A %d/%m/%Y, %H:%Mh")}")
        case 3:
            print(f"El número aleatorio generado es: {random.randint(1,10)}")
        case 4:
            print ("saliendo del programa... Hasta luego")
        case _:
            print("Opción inválida")
except ValueError:
    print("Debes introducir un número entre 1 y 4")

