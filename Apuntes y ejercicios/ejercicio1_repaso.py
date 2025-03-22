"""
Pedir al usuario un número entero. El programa nos tiene que decir si este número es divisible entre 2 y entre 3
"""


try:
    numero = int(input("Introduce un número entero para saber si es divisible entre 2 y/o 3: "))
    if numero % 2 == 0 and numero % 3 == 0:
        print(f"El número {numero} es divisible entre 2 y entre 3.")
    elif numero % 2 == 0 and numero % 3 != 0:
        print(f"El número {numero} es divisible entre 2 pero no entre 3.")
    elif numero % 2 != 0 and numero % 3 == 0:
        print(f"El número {numero} es divisible entre 3 pero no entre 2.")
    else:
        print(f"El número {numero} no es divisible ni entre 2 ni entre 3.")
except ValueError:
    print("Debes introducir un número entero.")