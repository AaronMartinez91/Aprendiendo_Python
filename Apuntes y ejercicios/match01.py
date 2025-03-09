# match con un número que represente un día de la semana y me devuelva el nombre del día

def weekday(n): # la n hace referencia a que acepta un número como entrada a la función
    match n:
        case 1: return "Lunes"
        case 2: return "Martes"
        case 3: return "Miércoles"
        case 4: return "Jueves"
        case 5: return "Viernes"
        case 6: return "Sábado"
        case 7: return "Domingo"
        case _: return "Nº de día inválido"

while True:
    try:
        dia = int(input("Introduce un valor del 1 al 7 para saber qué día de la semana es: "))
        print(f"El día {dia} corresponde al {weekday(dia)}")
    except ValueError:
        print("El valor introducido debe ser un número del 1 al 7")

