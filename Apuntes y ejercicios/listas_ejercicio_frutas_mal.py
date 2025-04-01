from random import choice
import os

# ! time os random

#! Simulación de una Máquina Tragaperras en Python

# Lista de Símbolos:

simbolos = ("\U0001F361","\U0001F364","\U0001F359")                  #?("\U0001F4B0","\U0001F3C6","\U00002B50") dinero, copa, estrella
print(simbolos)

# Saldo Inicial:
saldo_inicial = 100


# Funciones Necesarias:

# mostrar_menu(): Muestra un menú principal centrado con opciones para jugar, ver el saldo o salir del juego.

def mostrar_menu():
    print("\n" + "-" * 25)
    print("|     MENÚ DEL JUEGO     |")
    print("|------------------------|")
    print("| 1. Jugar               |")
    print("| 2. Ver el saldo        |")
    print("| 0. Salir del juego     |")
    print("-" * 25)


# mezclar_lista(lista): Mezcla la lista de símbolos de forma aleatoria. En este caso yo voy a hacer una función que devuelva un valor aleatorio de la tupla
def simbolo_aleatorio():
    return choice(simbolos)

simbolos_aleatorios = [simbolo_aleatorio(),simbolo_aleatorio(),simbolo_aleatorio()]
print(simbolos_aleatorios)

# verificar_ganador(lista): Verifica si todos los elementos de la lista son iguales, lo que indica que el jugador ha ganado.
def verificar_ganador(simbolos_aleatorios):
    if simbolos_aleatorios[0] == simbolos_aleatorios [1] == simbolos_aleatorios[3]:
        return True
    else:
        return False
# limpiar_pantalla(): Limpia la consola para mejorar la presentación visual del juego, es válido tanto para linux como para windows ya que usa la consola de comandos para hacerlo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# realizar_apuesta(): Permite al jugador ingresar una apuesta válida, asegurándose de que no exceda su saldo disponible.
def realizar_apuesta():
    if saldo_inicial <=0:
        print("No te queda saldo disponible.")
    else:
        apuesta = int(input("Introduce la cantidad de dinero que quieres apostar: "))
        if apuesta > saldo_inicial:
            print(f"No tienes suficiente saldo, el máximo que puedes apostar es {saldo_inicial}.")
        else:
            saldo_inicial =- apuesta


# actualizar_saldo(apuesta, ganador): Actualiza el saldo del jugador según el resultado de la ronda.
def actualizar_saldo():
    if verificar_ganador():
        saldo_inicial =+ apuesta
    

# simular_tragaperras(): Simula el efecto visual de una máquina tragaperras girando, mostrando varios estados intermedios antes de revelar el resultado final.



# Bucle Principal:


# Implementa un bucle principal que permita al jugador seleccionar entre jugar una ronda, ver su saldo actual o salir del juego.

# Si el jugador selecciona jugar, se realiza una apuesta, se simula la máquina tragaperras y se verifica si ha ganado.

# Si el jugador selecciona ver saldo, se muestra el saldo actual.

# Si el jugador selecciona salir, el programa finaliza.



# Validaciones:



# Asegúrate de que el jugador no pueda apostar más dinero del que tiene disponible.

# Si el saldo del jugador es 0, no se le permite realizar más apuestas.



# Interfaz Visual:



# El menú debe estar centrado y tener un marco exterior para mejorar la presentación.

# La simulación de la máquina tragaperras debe mostrar varios estados intermedios para crear un efecto visual de giro.








