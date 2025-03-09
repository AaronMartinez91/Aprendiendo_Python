"""
--------------        GENERADOR DE EMAILS          -----------------------------


Crear un programa en Python que a partir de los datos introducidos por

el usuario, el programa genere su dirección de email



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



Ampliación para conseguir el 9:

------------------------------

La empresa ha cambiado la política de creación de emails pasando a ser:

abroto@ifp.com

Crea otro programa que nos ayude a obtener este nuevo resultado



Ampliación para conseguir el 10:

-------------------------------

Hay usuarios que en su nombre o apellidos tienen accentos. 

Los emails, siguiendo la recomendación RFC 5322, no deberían llevar accentos ni caracteres especiales (á,à, ñ, ç, ä, etc)

Realizar un nuevo programa que elimine los acentos del nombre o del apellido 

(Ayuda: buscar información del módulo: unicodedata y el procedimiento:normalize o cualquier otro módulo parecido)


--------------------------------------------------------------------------------------
"""
import unicodedata

# Primera parte (con nombre completo)

nombre_completo = input("Por favor, introduzca su nombre completo: ")

nombre_empresa = input("Por favor, introduzca el nombre de la empresa: ")

dominio = ".com"

print(f"Su email de usuario es: {nombre_completo.strip().lower().replace(" ", ".") + "@" + nombre_empresa.strip().lower().replace(" ","") + dominio}")

# Primera parte (con la primera vocal del nombre + apellido completo), a este ya le aplico directamente la tercera parte con los acentos

nombre_completo2 = input("Por favor, introduzca su nombre completo: ")

nombre_empresa2 = input("Por favor, introduzca el nombre de la empresa: ")

dominio2 = ".com"

nombre_completo2_separado = nombre_completo2.strip().lower().split()

email_usuario = (nombre_completo2_separado[0][:1] + nombre_completo2_separado[1]) + "@" + nombre_empresa2.strip().lower().replace(" ","") + dominio2

# NFKD separa 'é' en 'e´', encode convierte el texto en bytes e ignora estos acentos o caracteres especiales que no existen. Por último, decode devuelve esos bytes a formato STR
normalizado = unicodedata.normalize('NFKD', email_usuario).encode('ASCII', 'ignore').decode('ASCII')

print(f"Su email de usuario es: {normalizado}")


