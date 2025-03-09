# Realizar un programa que realice la conversión de grados Fahrenheit a Centígrados: restar 32 y luego multiplicar por 5/ 9
# U+00B0 ° signo de grado, la escala va de 0 a 212, resultado con 2 decimales

while True:
    try:
        fahren = float(input("Introduce una temperatura en \U000000B0F para convertirla a \U000000B0C: "))
        while fahren < 0 or fahren >212:
            fahren = float(input("La escala de Fahrehheit tiene un rango de [0,212], introduce una temperatura correcta en \U000000B0F para convertirla a \U000000B0C: "))
            
        centigrados = (fahren-32)*(5/9)
        print(f"{fahren}\U000000B0F = {centigrados:.2f}\U000000B0C.")
    except ValueError:
        print("Debes introducir un valor correcto.")