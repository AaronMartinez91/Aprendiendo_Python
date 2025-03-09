try:
    edad = int(input("Introduce tu edad: "))
    es_adulto = "Sí" if edad >=18 else "No" # Operador TERNARIO, se pueden anidar varias condiciones pero no es recomendable, queda lioso
    print (f"¿Eres adulto? {es_adulto}")
except ValueError:
    print("Por favor, introduce un número correcto.")
# otro ejemplo:
a, b = 10, 20
mayor = a if a>b else b
print(f"el mayor de {a} y {b} es {mayor}") # suponemos que no pueden ser iguales

# Pedir al usuario un número y utilizando el operador ternario me diga si es par o impar

try:
    numero = float(input("Introduce un número para saber si es par o impar:"))
    resultado = "par" if numero%2==0 else "impar"
    print(f"El número {numero} es {resultado}")
except ValueError:
    print("Por favor, introduce un número.")   


# OPERADOR TERNARIO ANIDADO (a evitar)

edad = 25
mensaje = "Niño" if edad <12 else "Adolescente" if edad <18 else "Adulto"
