from random import choice
import os
import time


simbolos = ("\U0001F361","\U0001F364","\U0001F359") #! Tupla que contiene los símbolos sobre los que jugamos
saldo_inicial = 100 #! Tal y como me pide el enunciado empezaremos con un saldo inicial de 100
# seleccion = None #! Variable de control del bucle principal

#! función que muestra el menú con las distintas opciones
def mostrar_menu():
    print("\n" + "-" * 26)
    print("|     MENÚ DEL JUEGO     |")
    print("|------------------------|")
    print("| 1. Jugar               |")
    print("| 2. Ver el saldo        |")
    print("| 0. Salir del juego     |")
    print("-" * 26)


#! función que recoge un valor para poder trabajar con el menú
def seleccion_menu():
    #? Este bucle me permite recoger la respuesta correcta
    while True:
        seleccion = input(">> ")
        if seleccion in ("0","1","2"):
            limpiar_pantalla() #! Haciendo pruebas vi que si cerraba el programa después de ciertas condiciones dejaba "restos" de mensajes anteriores, así que aquí me aseguro de cerrarlo bien
            return int(seleccion)
        else:
            print("Opción no válida, por favor introduce un número que corresponda con una opción del menú: ", end="")
        

#! realizar_apuesta(): Permite al jugador ingresar una apuesta válida, asegurándose de que no exceda su saldo disponible.
def realizar_apuesta(saldo_actual):
    try:
        if saldo_actual <=0:
            print("No te queda saldo disponible.")
            return None #! Salimos del bucle sin realizar apuesta ya que sin dinero no debería poder apostar
        
        apuesta = int(input("Introduce la cantidad de dinero que quieres apostar o 0 para cancelar la apuesta: "))
        
        if apuesta == 0:
            return None #! Con esto aseguro una vuelta atrás si no se quiere apostar
        elif apuesta < 0:
            print("Por favor, introduce una cantidad positiva.")
        elif apuesta > saldo_actual:
            print(f"No tienes suficiente saldo, el máximo que puedes apostar es {saldo_actual}.")
        else:
            return apuesta
    except ValueError:
            print("Por favor, introduce un valor de apuesta correcto.")          

# #! función que crea una lista con randoms de la tupla "simbolos" // esta función ya no es necesaria ya que su funcionalidad está dentro de simular_tragaperras
# def simbolo_aleatorio():
#     return choice(simbolos)

# #! función que genera una lista con 3 símbolos aleatorios// venía de la mano con la anterior, así que tampoco hace falta ya
# def generar_lista_aleatoria():
#     return [simbolo_aleatorio() for _ in range(3)]

#! función que genera una lista con 3 valores aleatorios de la tupla inicial. Mientras la genera, va mostrando los cambios en la terminal con distinto tempo simulando una tragaperras
def simular_tragaperras():
    resultado = ["?", "?", "?"] #! Preparo la lista vacía sobre la que luego trabajaré

    #! Genero el valor del primer resultado mientras lo muestro repetidas veces para simular una ruleta
    for i in range(15):
        resultado[0] = choice(simbolos) #! La función choice escoge al azar un valor dentro de la tupla
        print(" | ".join(resultado), end="\r") #! con el método join creo una línea entre las distintas posiciones del array, con el \r sobreescribo el valor anterior
        time.sleep(0.1 if i < 5 else 0.3)  #! con el método sleep aplico un pequeño tiempo entre resultados, y controlando el iterador hago que los últimos valores salgan aún más lentos
    
    #! Segundo valor
    for i in range(15):
        resultado[1] = choice(simbolos)
        print(" | ".join(resultado), end="\r")
        time.sleep(0.1 if i < 5 else 0.3)
    
    #! Tercer valor
    for i in range(15):
        resultado[2] = choice(simbolos)
        print(" | ".join(resultado), end="\r")
        time.sleep(0.1 if i < 5 else 0.3)
    
    print(" | ".join(resultado))
    return resultado


#! verificar_ganador(lista): Verifica si todos los elementos de la lista son iguales, lo que indica que el jugador ha ganado.
def verificar_ganador(simbolos_aleatorios):
    if simbolos_aleatorios[0] == simbolos_aleatorios [1] == simbolos_aleatorios[2]:
        return True
    else:
        return False

#! actualizar_saldo(apuesta, ganador): Actualiza el saldo del jugador según el resultado de la ronda.
def actualizar_saldo(saldo,apuesta,ganador):
    if ganador:
        saldo += (apuesta*2)
        print(f"¡Enhorabuena, has ganado {apuesta*2}€!")
        return saldo
    else:
        saldo -= apuesta
        print(f"Lástima, has perdido {apuesta}€.")
        return saldo


#! limpiar_pantalla(): Limpia la consola para mejorar la presentación visual del juego, es válido tanto para linux como para windows ya que usa la consola de comandos para hacerlo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')




#! bucle principal

while True:
    limpiar_pantalla()
    mostrar_menu()
    seleccion = seleccion_menu()

    if seleccion == 0:
        print("\nCerrando el juego... \n¡Esperamos volver a verte pronto!")
        break
    elif seleccion == 1:
        apuesta = realizar_apuesta(saldo_inicial) #? Realizo una apuesta 

        if apuesta is not None: #! Tal y como he puesto antes, si la apuesta no era correcta me devolvía None, por lo que solo se puede jugar si la apuesta era válida
            simbolos_aleatorios = simular_tragaperras() #? Genero una lista (juego)
            ganador = verificar_ganador(simbolos_aleatorios) #? compruebo si la lista es o no de victoria
            saldo_inicial = actualizar_saldo(saldo_inicial,apuesta,ganador) #? en función del resultado de la apuesta actualizo el saldo y lo muestro
        input("\nPresiona Enter para continuar.") #! es importante aquí marcar un "tope", ya que me continuaría con el bucle y el limpiar pantalla del principio del mismo borraría esta info

    elif seleccion ==2:
        print(f"Su saldo actual es de {saldo_inicial}€")
        input("\nPresiona Enter para continuar.") 
