
#! ------------------------------------------     FUNCIONES     ------------------------------------------


# Una función es un bloque de código REUTILIZABLE
# Ventajas: 
    # - Es REUTILIZABLE: Evita repetir código
    # - Es MODULAR: Divide el programa en bloques lógicos, UNA FUNCIÓN -> UNA COSA
    # - FACILIDAD DE MANTENIMIENTO: Cambiar una función SOLO afecta a esa parte del código
    # - LEGIBILIDAD: facilita el entendimiento del código



def saludar():
    print("Hola Mundo!")

# Invoco a la función (es decir, la llamo)
saludar()

def saludar_persona(nombre): # ? función que recibe un PARÁMETRO (variable que esta recibe para operar)
    print(f"Hola, {nombre}.")

saludar_persona("Aarón") # le paso un ARGUMENTO (valor real que paso a una función)

#! Realizar una función que sume dos números

def suma(a,b): # suma 2 parámetros
    return a+b #! OJO! SI NO PONGO RETURN DEVUELVE NONE, YA QUE LA FUNCIÓN NO ALMACENA NI DEVUELVE NADA

x,y = 2,3
print(f"La suma de {x} + {y} es {suma(x,y)}")

#! Realizar una función que dice si un número es par o impar

def es_par(numero):
    if numero % 2 == 0:
        return "Par"
    return "Impar"

num = int(input("Introduce un número entero para ver si es par o no: "))
print(f"El número {num} es {es_par(num)}")

#! Realizar una función que divida dos números, se llamará "dividir" y aceptará dos parámetros: a,b

def dividir(a,b):
    if b == 0:  #? es importante controlar la división entre 0
        return "Infinito"
    return a/b

# def dividir(a,b):
#     try: 
#         return a/b    #? controlando división entre 0 pero con try/except
#     except ZeroDivisionError:
#         return "Error: división entre 0"

x = float(input("Introduce el dividendo: "))
y = float(input("Introduce el divisor: "))

print(f"El resultado de dividir {x} entre {y} es de : {dividir(x,y)}")