
#! Variables globales y locales

mensaje = "Hola... desde variable global"

def mostrar_mensaje():
    mensaje = "Hola... desde la función (variable local)"
    print(mensaje)

mostrar_mensaje()
print(mensaje)

