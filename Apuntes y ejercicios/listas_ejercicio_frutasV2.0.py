
#! Para esta versión, voy a utilizar el código de la V1.0 pero haciendo varios cambios:
    #? - Tendremos una matriz de 3x3 en lugar de una lista de 3 valores
    #? - Cada símbolo tendrá un valor de premio distinto
    #? - Habrá combinaciones de premios, no solo estará la línea horizontal, sino que también habrá diagonales (para ello tendré que simular los giros como si fueran 3 ruletas)
    #? - Las combinaciones de premios anteriores darán un extra de bonificación si ocurren de forma simultánea


from random import choice
import os
import time


# simbolos = ("\U0001F361","\U0001F364","\U0001F359") sustituida por el diccionario #! Tupla que contiene los símbolos sobre los que jugamos (🍡,🍤,🍙)
saldo_inicial = 100 #! Tal y como me pide el enunciado empezaremos con un saldo inicial de 100
PREMIO_SIMBOLOS = {  #! Este diccionario contiene el valor del premio de cada uno de los elementos en caso de que hagamos una línea con ellos, puesto que este contiene la info de la tupla inicial, ya no la necesitamos
    "\U0001F361" : 0.5,
    "\U0001F364" : 1.0,
    "\U0001F359" : 0.2
}

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
    if saldo_actual <=0:
        print("No te queda saldo disponible.")
        return None #! Salimos del bucle sin realizar apuesta ya que sin dinero no debería poder apostar
    while True: #? voy a mejorar un poco esta salida del programa para no tener que volver a empezar cada vez que me dan un valor incorrecto    
        try:
            apuesta = float(input("Introduce la cantidad de dinero que quieres apostar o 0 para cancelar la apuesta: "))
            
            if apuesta == 0:
                return None #! Con esto aseguro una vuelta atrás si no se quiere apostar
            elif apuesta < 0:
                print("Por favor, introduce una cantidad positiva.")
            elif apuesta > saldo_actual:
                print(f"No tienes suficiente saldo, el máximo que puedes apostar es {saldo_actual:.2f}.")
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

#! función que genera una matriz con 3x3 valores aleatorios del diccionario inicial. Mientras la genera, va mostrando los cambios en la terminal con distinto tempo simulando una tragaperras
def simular_tragaperras():
    resultado = [["?", "?", "?"],["?", "?", "?"],["?", "?", "?"]] #! Preparo la lista vacía sobre la que luego trabajaré, en este caso una matriz de 3x3
    # ? tal y como he comentado al principio, voy a hacer que giren 3 "ruletas verticales" emulando una tragaperras real.
    
    for col in range(3):  #? debo hacer 3 vueltas (3 columnas)
        for i in range(15): #? sigo con las 15 iteraciones para simular el giro (ralentizando al final)
            for fila in range(3):  #? En cada iteración genero los valores de las filas
                resultado[fila][col] = choice(list(PREMIO_SIMBOLOS.keys()))
            
            #? Al generar 3 valores a la vez, no quedaba estético de la forma anterior, así que reutilizo mi función de limpiar pantalla en cada vuelta
            limpiar_pantalla()

            #? la muestro
            for fila in resultado:
                print(" | ".join(fila))
            
            time.sleep(0.1 if i < 5 else 0.3)  # Giro más lento al final

    print()  
    return resultado

#! verificar_ganador(lista): Verifica si hay líneas o diagonales que generen premio y devuelve el multiplicador del premio además de si hay combo (varias líneas premiadas)
#? como en este caso voy a sumar y hacer cálculos más complejos de los premios, esta función va a determinar ya si hay premio o no y el total correspondiente, por ello es aquí donde también mostraremos por pantalla el resultado de cada línea, así como el premio total. Simplificando la función actualizar_saldo()
def verificar_ganador(matriz_generada, apuesta):
    premio_total = 0 #? con esta variable controlo el premio final, sumando en ella cada valor que saque de cada cálculo por línea
    combos = 0 #? variable que aumenta el premio si hay varias combinaciones de victoria a la vez

    if matriz_generada[0][0] == matriz_generada[0][1] == matriz_generada[0][2]: #? comparo los valores de la línea
        simbolo = matriz_generada[0][0] #? creo una variable que almacena el símbolo que la forma (con pillar uno me sirve ya que los 3 son iguales)
        premio_parcial = apuesta * PREMIO_SIMBOLOS[simbolo] #? asigno el valor al multiplicador del símbolo que corresponde con el diccionario
        premio_total += premio_parcial #? sumo lo ganado en esta combinación 
        combos += 1 #? añado 1 al multiplicador de combos
        print(f"¡Línea ganadora! {simbolo*3} -> +{premio_parcial:.2f}€")
    
    if matriz_generada[1][0] == matriz_generada[1][1] == matriz_generada[1][2]:
        simbolo = matriz_generada[1][0]
        premio_parcial = apuesta * PREMIO_SIMBOLOS[simbolo]
        premio_total += premio_parcial 
        combos += 1
        print(f"¡Línea ganadora! {simbolo*3} -> +{premio_parcial:.2f}€")
    
    if matriz_generada[2][0] == matriz_generada[2][1] == matriz_generada[2][2]:
        simbolo = matriz_generada[2][0]
        premio_parcial = apuesta * PREMIO_SIMBOLOS[simbolo]
        premio_total += premio_parcial 
        combos += 1
        print(f"¡Línea ganadora! {simbolo*3} -> +{premio_parcial:.2f}€")
   
    if matriz_generada[0][0] == matriz_generada[1][1] == matriz_generada[2][2]:
        simbolo = matriz_generada[0][0]
        premio_parcial = apuesta * PREMIO_SIMBOLOS[simbolo]
        premio_total += premio_parcial 
        combos += 1
        print(f"¡Línea ganadora! {simbolo*3} -> +{premio_parcial:.2f}€")
    
    if matriz_generada[0][2] == matriz_generada[1][1] == matriz_generada[2][0]:
        simbolo = matriz_generada[0][2]
        premio_parcial = apuesta * PREMIO_SIMBOLOS[simbolo]
        premio_total += premio_parcial 
        combos += 1
        print(f"¡Línea ganadora! {simbolo*3} -> +{premio_parcial:.2f}€")

    #? si tenemos más de una línea ganadora, muestro también el premio final
    if combos > 1: 
        premio_total *= combos
        print(f"¡Bonus x {combos} combos! Has ganado un súper premio de {premio_total:.2f}€")

    #? una vez hechos todos los cálculos y mostrado los premios (si los hay), devuelvo en caso positivo el valor (no muestro nada ya que lo he hecho previamente)
    if combos > 0:
        return premio_total
    #? en caso de que no haya habido premio, lo que devuelvo es el valor negativo de la apuesta con un mensaje de derrota.
    else:
        print(f"Lástima, has perdido {apuesta:.2f}€.")
        return -apuesta

#! actualizar_saldo(saldo, premio): Actualiza el saldo del jugador según el resultado de la ronda, en este caso el premio puede ser negativo por lo que ya no necesito la apuesta
def actualizar_saldo(saldo,premio):
    #? como ya no tengo solo una condición booleana de "hay victoria o no la hay", cambio la lógica de la función:
    saldo += premio
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
            simbolos_aleatorios = simular_tragaperras() #? Genero una matriz con moviemiento (juego)
            ganador = verificar_ganador(simbolos_aleatorios, apuesta) #? compruebo si la lista es o no de victoria y aplico premios, además de mostrar el pantalla el resultado
            saldo_inicial = actualizar_saldo(saldo_inicial,ganador) #? en función del resultado de la apuesta actualizo el saldo y lo muestro
        input("\nPresiona Enter para continuar.") #! es importante aquí marcar un "tope", ya que me continuaría con el bucle y el limpiar pantalla del principio del mismo borraría esta info

    elif seleccion ==2:
        print(f"Su saldo actual es de {saldo_inicial:.2f}€")
        input("\nPresiona Enter para continuar.") 
