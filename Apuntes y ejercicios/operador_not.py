# Revisar si una variable está dentro del rango [1,10]

dato = int(input("Introduce un número entero [1,10]: "))  # Al ponerlo de esta forma asumimos que ambos números están incluidos

if dato <1 or dato >10:
   esta_dentro_rango=False
else:
   esta_dentro_rango=True

if not esta_dentro_rango: # es muy simplificable pero así usamos el "not"
   print(f"La variable introducida por el usuario es {dato} y NO está DENTRO del rango [1,10]")   
else:
   print(f"La variable introducida por el usuario es {dato} y está DENTRO del rango [1,10]")   