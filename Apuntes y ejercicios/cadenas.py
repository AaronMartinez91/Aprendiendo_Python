# una cadena en Python es un conjunto de caracteres

cadena2 = ''' Python
                    no
                        me
                            parece tan complicado'''
cadena3 = """   OTRA
 CADENA
      EN
        PYTHON
   """
# print(cadena1)
# print(cadena2)
# print(cadena3)

# Acceder a un elemento de la cadena

cadena1 = "Hola Mundo!"
print("Accedo al primer elemento de la cadena1:",cadena1[0])
print("Accedo al quinto elemento de la cadena1:",cadena1[5])
# print("Accedo al quinto elemento de la cadena1:",cadena1[22]) "IndexError: string index out of range" :la cadena no tiene 22 caracteres
print("Accedo al último elemento de la cadena1:", cadena1[-1])
print("Accedo al penúltimo elemento de la cadena1:", cadena1[-2])

# El método o función para saber la longitud de la cadena
print(f"La longitud de la cadena1 es: {len(cadena1)}") # esto da 11, ya que aunque llamemos 0 al primero, sigue siendo un caracter

# Ejerccio: Acceder al último elemento de la cadena, utilizando SÓLO la función len()
nombre = "Aarón"
ultimo = len(nombre)
print(f"El último caracter de la cadena nombre es: {nombre[ultimo-1]}")
# print(f"El último caracter de la cadena nombre es: {nombre[ultimo]-1}") este no funciona porque le estás restando 1 a un caracter ya fuera de rango

# a pesar de todo, la opción más correcta sería aplicarle ya el -1 a último, para aplicar directamente siempre la variable de forma correcta (hay que recordar que empieza a contar por 0)

# concatenación de cadenas
nombre = "Aarón"
apellido = "Martínez"
concatenacion = nombre + apellido #podemos guarrearlo con un + " " en medio
print(concatenacion) # no deja espacios ya que las "une" directamente

# utilizando el método join
concatenacion = ''.join([nombre,' ',apellido]) #como le estoy aplicando una función, tengo que poner "algo" siempre delante. por eso le pongo las '' vacías, para que no ponga nada extra
print(concatenacion)

# f-strings
print(f"Hola {nombre}, tu apellido es: {apellido}.")

# métodos o funciones de cadenas

cadena = "Hola Mundo"
print(f"Cadena original: {cadena}")
print(f"Cadena en mayúsculas: {cadena.upper()}")
print(f"Cadena en minúsculas: {cadena.lower()}")

password = "  1234    "
print(f"Tu contraseña es: {password.strip()}") # el método strip elimina espacios iniciales y finales

ciudad = "    BarCeLoNa     "

print(f"Vives en: {ciudad.strip().lower()}")