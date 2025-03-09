"""
Dada la siguiente cadena:
cadena = "abcdefg"
Extrae las siguientes letras usando slicing:
1.- 'bc'
2.- 'de'
3.- 'ace'
4.- 'fg'
5.- 'abcdef'
6.- 'gfedcba'
"""

cadena = "abcdefg"

print(f"bc = {cadena[1:3]}")
print(f"de = {cadena[3:5]}")
print(f"ace = {cadena[:5:2]}")    # ya que saltamos de 2 en 2 tanto da 5 o 6, ambos no llegan a la siguiente letra
print(f"fg = {cadena[5:7]}")      # también podemos hacerlo empezando desde atrás con cadena[-2:]
print(f"abcdef = {cadena[:-1]}")  # también se puede hacer empezando desde el principio cadena[:6]
print(f"gfedcba = {cadena[::-1]}")

"""
Dada la siguiente cadena:
cadena = "0123456789"
Extrae las siguientes letras usando slicing, con 3 números y el :: de en medio vacío, ejemplo: 1::2 (el último no se puede)
1.- '13579'
2.- '02468'
3.- '246'
"""
cadena2 = "0123456789"

print(f"13579 = {cadena2[1::2]}")
print(f"02468 = {cadena2[::2]}")
print(f"246 = {cadena2[2:7:2]}")

#dada la cadena cadena3 = "Hola, mundo!" obtén su longitud usando una función

cadena3 = "Hola, mundo!"

print(f"La longitud de la cadena: '{cadena3}' es: {len(cadena3)}")   # la comilla simple queda "por debajo" de la doble, pero me dejaría ponerlo
print(f"La longitud de la cadena: \"{cadena3}\" es: {len(cadena3)}") # sin embargo, puedo poner una "" si le pongo una \ antes de cada una de ellas

# dada la cadena4 = "abcdefghij", obtén la primera mitad de la cadena usando variables

cadena4 = "abcdefghij"

mitad_cadena4 = int(len(cadena4)/2) 
mitad_cadena4 = len(cadena4)//2       # // es una división entera, lo que ya nos devuelve un int 

mitad_cadena5 = len(cadena4)
print(f"Tipo de dato de la cadena con len sin dividir después: {type(mitad_cadena5)}")

mitad_cadena6 = len(cadena4)/2
print(f"Tipo de dato de la cadena con len si dividimos después de usarla: {type(mitad_cadena6)}")

print(f"abcde = {cadena4[:mitad_cadena4]}")         # para poder usar el slice, la variable debe ser un INTEGER, y la función len me devuelve un float ya que he dividido antes
print(f"abcde = {cadena4[:int(len(cadena4)/2)]}")   # no es necesario crear la variable, podemos hacerlo todo directamente en la misma línea si controlamos el tipo de dato, aunque es lioso

# la otra mitad:

print(f"fghij = {cadena4[mitad_cadena4:]}")
