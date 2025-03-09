"""
Una tienda aplica descuentos según el monto de la compra de un cliente y posteriormente calcula el IVA del 21%.

Reglas de descuento:
Menos de 50€ → No hay descuento.
Entre 50€ y 100€ → 5% de descuento.
Entre 100€ y 200€ → 10% de descuento.
Más de 200€ → 15% de descuento.
Tareas del programa:
Pedir el total de la compra al usuario.
Aplicar el descuento correspondiente.
Calcular el IVA (21%) sobre el total con descuento.
Mostrar el descuento aplicado, el total sin IVA y el total final con IVA.
Manejar errores si el usuario introduce un valor negativo o no numérico.
"""

try: # una vez más, controlo que lo que introduzcan sean los valores que busco
    # Empezamos pidiendo el dato al usuario para tener la variable con la que operar
    total_inicial = float(input("Por favor, introduzca el precio final de la compra: "))
    # Ahora tengo que valorar si le hago o no descuento
    if total_inicial < 0:
        print("Revise el importe introducido, ya que este no puede ser negativo")
    elif total_inicial == 0:
        print("Revise el importe introducido, ya que este no puede ser 0.")
    else:
        if total_inicial < 50:
            total_con_descuento = total_inicial
            descuento = 0
        elif total_inicial < 100: # puesto que ya vengo de controlar el < 50, no necesito aplicar aquí la condición de >=50
            total_con_descuento = total_inicial * 0.95
            descuento = 5 # como debo mostrar el porcentaje del descuento, creo la variable y le asigno el valor en función del valor
        elif total_inicial < 200:
            total_con_descuento = total_inicial * 0.9
            descuento = 10
        else:
            total_con_descuento = total_inicial * 0.85
            descuento = 15
        total_final = total_con_descuento * 1.21 #toda esta parte la tengo dentro del else, ya que solo quiero que se cumpla si los valores eran correctos
        # Una vez tengo calculados los valores, procedo a mostrarlos por pantalla
        print(f"Precio inicial de la compra: {total_inicial:.2f}€.\n  Descuento aplicado: {descuento}%.\n  Total a pagar sin IVA: {total_con_descuento:.2f}€.\n  Total a pagar con IVA: {total_final:.2f}€")
except ValueError:
    print("Por favor, introduzca un valor correcto.")

