"""
Escribe un programa para extraer cada dígito de un número entero en orden inverso.
Por ejemplo, si el número entero dado es 7536, la salida debe ser "6 3 5 7", con un espacio separando los dígitos
"""
numero = input("Introduce un número: ")
print(f"El número introducido es {numero} y es de tipo {type(numero)}")

numero_invertido = numero[::-1]

print(f"El número \"{numero}\" separado e invertido es: {" ".join(numero_invertido)}")   # con la función join separo cada elemento del string con lo que yo le quiera poner en medio
print(f"El número \"{numero}\" separado e invertido es: {"💀".join(numero_invertido)}")  # se puede hacer incluso con emoticonos