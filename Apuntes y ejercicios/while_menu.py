def mostrar_menu():
    print("Menú: ")
    print("1.- Opción 1")
    print("2.- Opción 2")
    print("3.- Opción 3")
    print("4.- Salir")

opcion = 0

while opcion != 4:
    mostrar_menu()
    try:
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1 :
            print ("Has seleccionado la opción 1")
        elif opcion == 2:
            print ("Has seleccionado la opción 2")
        elif opcion == 3:
            print ("Has seleccionado la opción 3")
        elif opcion == 4:
            print ("Saliendo del menú")
        else:
            print ("Opción no válida, por favor inténtelo de nuevo")
    except ValueError:
        print("Debes introducir un número.")
print("Has salido del programa")