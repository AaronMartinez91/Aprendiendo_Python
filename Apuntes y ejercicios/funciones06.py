
#! docstring (documento string) --> ayuda interna que se utiliza para explicar qué hace la función

def suma(a,b):
    """
    Suma de dos números y devuelve su resultado

    Parámetros:
      a (int o float) : primer número
      b (int o float) : segundo número

    Devuelve:
        int o float: resultado de la suma
    """
    return a+b

help (suma)  #? devuelve lo que está entre comillas
print(suma(2,5))