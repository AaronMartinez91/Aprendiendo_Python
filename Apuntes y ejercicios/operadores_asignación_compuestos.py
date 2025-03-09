valor = int(input("Introduce un número: ")) # con el input es una CADENA!!
# Multiplicar por 3

# valor = valor * 3  forma tradicional
valor *= 3  

# Divir entre 5
valor /= 5 # da un float
valor //= 5 # da un int ignorando el decimal
print(valor)

# Módulo de 3(saca el resto)
valor %= 3

# si lo quiero poner en una variable debo seararlo y ya no necesito el =
resultado = valor%3
print(f"El resto de divir {valor} entre 3 es {resultado}")

# elevar un número al cubo de un valor entero introducido por el usuario
valor = int(input("Introduce un número: "))
valor **=3
print(f"El cubo {valor}")