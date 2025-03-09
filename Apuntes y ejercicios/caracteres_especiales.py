# Carácteresespeciales

print("Hola \nClase") # Igual que en C, salto de línea
print("\t\t Hola \t que \t tal") # tabulador o secuencia escape
print('Ca l\' Àngela') # con la contrabarra hacemos que nos lea el ' y no nos rompa la cadena
print("c:\\nombre\\tributos") # al querer usar la contrabarra, en este caso nos metería un \n y un \t, por lo que debo poner \\
print("😢") # con win+. llego a los emoticonos de windows. También puedo buscar online alguno en UNICODE (symbl.cc)
print("\U00002764") # Aquí con el unicode en lugar de copiar el emoji U+2764, pero python quiere \U y 8 dígitos, así que rellenamos con 0s