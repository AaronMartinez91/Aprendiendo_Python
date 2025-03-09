# Realizar un programa que pida una nota [0,10], (match case)
# si nota <5 suspendido 
# si nota mayor o igual a 5 e inferior a 7 bien 
# si nota igual o mayor a 7 e inferior a 9 notable
# si nota mayor o igual a 9 e inferior a 10 excelente
# si 10 matrícula de honor
# en cualquier otro caso nota fuera de rango

try:
    nota = float(input("¿Qué nota has sacado?: "))
    while nota <0 or nota >10:
        nota = float(input("Introduce la nota real o te pongo un 0: "))
    match nota:
        case 0:
            print("La inteligencia te persigue, pero tú eres más rápido")
        case _ if 0< nota <5: # el case _ me permite poner un condicional detrás
            resultado = "Suspendido🤦‍♀️"
        case _ if 5<= nota <7:
            resultado = "Bien🙂"
        case _ if 7<= nota <9:
            resultado = "Notable👍"
        case _ if 9<= nota <10:
            resultado = "Excelente😁"
        case 10:
            resultado = "Matrícula de honor😎" 
        case _: 
            resultado = "El dato introducido es incorrecto"
    print(resultado)
except ValueError:
    print("¿De verdad no eres capaz ni de poner un número entre el 0 y el 10? Aquí tienes tu 0, campeón😒")
