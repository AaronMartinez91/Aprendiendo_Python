import unicodedata

"""
--------------        GENERADOR DE EMAILS          -----------------------------
Crear un programa en Python que a partir de los datos introducidos por el usuario, el programa genere su dirección de email

Ejemplo:

-------

nombre_competo ="     Angel Broto   "

nombre_empresa="  iFP  "

dominio=".com"

Resultado:  angel.broto@ifp.com

-----------------------------------------------------------------------------------------------

PASOS A SEGUIR:

1.- Crear la variable 'nombre_completo' con el nombre y apellido del usuario (sin acentos)

2.- Crear la variable 'nombre_empresa' con el nombre donde trabaja el usuario

3.- Crear la variable 'dominio' con el dominio (.es, .com , etc) de la empresa  

4.- Generar el email del usuario

"""

nombre_completo = input("Por favor, introduzca su nombre completo: ")

nombre_empresa = input("Por favor, introduzca el nombre de la empresa: ")

dominio = ".com"

# una vez tengo los datos, debo darles el formato necesario. Primero debo eliminar los espacios y ponerlo en minúsculas

nombre_completo_junto = nombre_completo.strip().lower()

# print(nombre_completo_junto)  aquí veo que solo me falta el punto, ahora lo sustituyo

nombre_completo_junto_final = nombre_completo_junto.replace(" ", ".")

# print(nombre_completo_junto_final) aquí veo que lo he convertido correctamente, todo podría hacerlo en una misma línea, pero así lo veo más claro

# hacemos lo mismo con el nombre de la empresa pero sin el "." esta vez en una línea para cambiar

nombre_empresa_final = nombre_empresa.strip().lower().replace(" ","")

# print(nombre_empresa_final) compruebo que está correcto

# por último debo unir las 3 variables en una

email_usuario = nombre_completo_junto_final + "@" + nombre_empresa_final + dominio


print(f"Su email de usuario es: {email_usuario}")


"""
Ampliación para conseguir el 9:

------------------------------

La empresa ha cambiado la política de creación de emails pasando a ser:

abroto@ifp.com

Crea otro programa que nos ayude a obtener este nuevo resultado
"""
# seguimos la misma lógica pero en este caso usaremos split para quedarnos solo con la parte que nos interesa

nombre_completo2 = input("Por favor, introduzca su nombre completo: ")

nombre_empresa2 = input("Por favor, introduzca el nombre de la empresa: ")

dominio2 = ".com"

# en este caso debemos separar el nombre completo en 2 partes para poder utilizar la primera y aplicarle el strip

nombre_completo2_separado = nombre_completo2.strip().lower().split()

# print(nombre_completo2_separado) compruebo que me ha separado y eliminado los espacios, además de pasarlo a minúsculas

# print(nombre_completo2_separado[0][:1]) compruebo que esto corresponde a lo que busco, es decir, la primera letra de la primera parte de la lista

nombre_completo_junto_final2 = nombre_completo2_separado[0][:1] + nombre_completo2_separado[1]

# print(nombre_completo_junto_final2) comprobación, una vez más

#seguimos la lógica del ejercicio anterior para llegar al resultado final con la segunda parte

nombre_empresa_final2 = nombre_empresa2.strip().lower().replace(" ","")

email_usuario2 = nombre_completo_junto_final2 + "@" + nombre_empresa_final2 + dominio2

print(f"Su email de usuario es: {email_usuario2}")

"""
Ampliación para conseguir el 10:

-------------------------------

Hay usuarios que en su nombre o apellidos tienen accentos. 

Los emails, siguiendo la recomendación RFC 5322, no deberían llevar accentos ni caracteres especiales (á,à, ñ, ç, ä, etc)

Realizar un nuevo programa que elimine los acentos del nombre o del apellido 

(Ayuda: buscar información del módulo: unicodedata y el procedimiento:normalize o cualquier otro módulo parecido)


--------------------------------------------------------------------------------------

https://docs.python.org/es/3/
"""

# si no lo he entendido mal, el normalize nos devuelve el equivalente "sin acentos" de cada letra, y debemos importar la librería para usarlo (lo hago al principio de todo)

# NFKD separa 'é' en 'e´', encode convierte el texto en bytes e ignora estos acentos o caracteres especiales que no existen. Por último, decode devuelve esos bytes a formato STR
normalizado = unicodedata.normalize('NFKD', email_usuario2).encode('ASCII', 'ignore').decode('ASCII')

print(f"Su email de usuario es: {email_usuario2}")