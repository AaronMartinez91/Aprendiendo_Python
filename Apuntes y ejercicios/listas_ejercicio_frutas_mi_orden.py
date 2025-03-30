from random import choice
import os

seleccion = -2
simbolos = ("\U0001F361","\U0001F364","\U0001F359") 
saldo_inicial = 100

#! función que muestra el menú con las distintas opciones
def mostrar_menu():
    print("\n" + "-" * 25)
    print("|     MENÚ DEL JUEGO     |")
    print("|------------------------|")
    print("| 1. Jugar               |")
    print("| 2. Ver el saldo        |")
    print("| 0. Salir del juego     |")
    print("-" * 25)
    return input(">> ") #? no solo mostramos el menú sino que ya esperamos una respuesta al mismo

#! realizar_apuesta(): Permite al jugador ingresar una apuesta válida, asegurándose de que no exceda su saldo disponible.
def realizar_apuesta():
    if saldo_inicial <=0:
        print("No te queda saldo disponible.")
    else:
        apuesta = int(input("Introduce la cantidad de dinero que quieres apostar: "))
        if apuesta > saldo_inicial:
            print(f"No tienes suficiente saldo, el máximo que puedes apostar es {saldo_inicial}.")
        else:
            return apuesta  

#! función que crea una lista con randoms de la tupla "simbolos"
def simbolo_aleatorio():
    return choice(simbolos)

#! función que genera una lista con 3 símbolos aleatorios
def generar_lista_aleatoria():
    return [simbolo_aleatorio() for _ in range(3)]


#! verificar_ganador(lista): Verifica si todos los elementos de la lista son iguales, lo que indica que el jugador ha ganado.
def verificar_ganador(simbolos_aleatorios):
    if simbolos_aleatorios[0] == simbolos_aleatorios [1] == simbolos_aleatorios[2]:
        return True
    else:
        return False

#! actualizar_saldo(apuesta, ganador): Actualiza el saldo del jugador según el resultado de la ronda.
def actualizar_saldo(saldo_inicial,apuesta,ganador):
    if ganador:
        saldo_inicial += (apuesta*2)
        print(f"¡Enhorabuena, has ganado {apuesta*2}€!")
        return saldo_inicial
    else:
        saldo_inicial -= apuesta
        print(f"Lástima, has perdido {apuesta}€.")
        return saldo_inicial


#! limpiar_pantalla(): Limpia la consola para mejorar la presentación visual del juego, es válido tanto para linux como para windows ya que usa la consola de comandos para hacerlo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')




#! bucle principal

while seleccion != 0:
    seleccion = int(mostrar_menu())
    if seleccion == 1:
        apuesta = realizar_apuesta() #? Realizo una apuesta (lo permito o no) y almaceno el valor
        simbolos_aleatorios = generar_lista_aleatoria() #? Genero una lista (juego)
        ganador = verificar_ganador(simbolos_aleatorios) #? compruebo si la lista es o no de victoria
        saldo_inicial = actualizar_saldo(saldo_inicial,apuesta,ganador) #? en función del resultado de la apuesta actualizo el saldo y lo muestro
        limpiar_pantalla()
    elif seleccion ==2:
        print(f"Su saldo actual es de {saldo_inicial}€")