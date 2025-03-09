tengo_dinero=False
tengo_vacaciones=False

if (tengo_dinero or tengo_vacaciones):  # el tengo_dinero==True es innecesario. ya lo asume python
    print("Me voy a Cancun de vacaciones")
elif (tengo_dinero or not tengo_vacaciones):
    print("Me voy a comer cada día al restaurante")
elif (not tengo_dinero or tengo_vacaciones):
    print("Me quedo todo el día en casa vicioro al yakuza")
else: # not tengo_dinero or not tengo_vacaciones
    print("Haber estudiao")

    # con esta lógica, deberían salir los 3 últimos print pero NO SALEN POR SER UN ELIF/ELSE  en lugar de un if