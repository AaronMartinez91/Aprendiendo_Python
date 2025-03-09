# Operador lógico AND (y) devuelve un True si ambos valores a evaluar son verdaderos

condicion1 = True #OJO, True y False SIEMPRE TIENEN LA PRIMERA LETRA EN MAYÚSCULA
condicion2 = True

resultado = condicion1 and condicion2
print (f"El resultado de {condicion1} and {condicion2} = {resultado}") # Es cierto porque ambas variables son ciertas

condicion3 = False
resultado2 = condicion1 and condicion3
print (f"El resultado de {condicion1} and {condicion3} = {resultado2}") # Es falso porque ambas variables no son ciertas

# Ejercicio: Pedir al usuario un número entre 10 y 50

numero = int(input("Introduce un número entre 10 y 50: "))

# Verificar si el número está dentro del rango
if numero >=10 and numero <=50:
    print("👍 El número está dentro del rango")
else:
    print("😒 ¿Seguro que tus padres no son hermanos?")

#----------------------------------------------------------------------------------------------------

tengo_dinero=False
tengo_vacaciones=False

if (tengo_dinero and tengo_vacaciones):  # el tengo_dinero==True es innecesario. ya lo asume python
    print("Me voy a Cancun de vacaciones")
elif (tengo_dinero and not tengo_vacaciones):
    print("Me voy a comer cada día al restaurante")
elif (not tengo_dinero and tengo_vacaciones):
    print("Me quedo todo el día en casa viciando al yakuza")
else: # not tengo_dinero and not tengo_vacaciones
    print("Haber estudiao")