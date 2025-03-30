
#! Pedir al usuario que introduzca las notas de diferentes módulos [0,10]. El programa tiene que calcular y mostrar la media de las notas (con dos decimales) introucidas. Me dirá también si he aprobado o no. 
#! Crear el array calificaciones[]. 

calificaciones =[]
cantidad_notas = None # le doy un valor para controlar el bucle posterior y asegurarme de que recoge el valor que quiero
while cantidad_notas is None:
    try:
        cantidad_notas = int(input("¿Cuántas notas distintas tienes?: "))
        if cantidad_notas <= 0:
            print("El número de notas debe ser mayor que 0.")
            cantidad_notas = None # si el valor introducido es 0 no puedo trabajar con él pero sigue siendo un int, por eso lo controlo y devuelvo None, así no salgo del bucle
    except ValueError:
        print("Debes introducir un número entero.") # si el valor no era correcto, muestro el mensaje, sigue siendo None y vuelve a empezar el bucle

for _ in range (cantidad_notas):
    nota = None # Vuelvo a usar el método de antes para asegurarme de que recojo la variable como la necesito
    while nota is None:
        try:
            nota = float(input("Introduce la nota en base a 10: "))
            if nota <0 or nota > 10:
                print("La nota debe ser entre 0 y 10, por favor, vuelve a introducirla: ")
                nota = None
        except ValueError:
            print("Debes introducir un número válido.")        
    calificaciones.append(nota) # como aquí le añado el valor "nota" a la lista, ya puedo resetearla en la siguiente vuelta para seguir con el bucle

# ? calculo media
suma_calificaciones = 0
for calificacion in calificaciones:
    suma_calificaciones += calificacion
media = suma_calificaciones / cantidad_notas

#? muestro mensaje en función del resultado de la media
if media >= 5:
    print(f"Enhorabuena, has aprobado con un {media:.2f}.")
else:
    print(f"☹️ ¡Haber estudiao! Has suspendido con un {media:.2f}.")