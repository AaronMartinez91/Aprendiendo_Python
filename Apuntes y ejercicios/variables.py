# variables en Python

a = 3 # asignamos a la variable 'a' el número entero '3'
nombre = "Aarón"
edad = 33 
altura = 1.67
is_Alumno = True

print ("Te llamas", nombre) # concatenamos
print (f"Te llamas {nombre}, tienes {edad} años y mides {altura:.3f} metros y eres alumno: {is_Alumno}.") # la 'f' indica que todo es una cadena y que lo que ponga entre {} será una variable
comentario ="""
 esto
    es
            una
                introducción
                a
                                python"""
print(comentario) #respeta los espacios e indentaciones

# reglas de nomenclatura de las variables

"""
    1.- Deben empezar siempre por: "_" o una letra
    2.- El resto puede ser (a-z, A-Z, 0-9)
    3.- Podemos utilizar caracteres como la 'ñ', pero no es recomenable ya que no está en todos los idiomas
    4.- NO podemos utilizar palabras reservadas (for, while, print...)
    5.- Python es CASE SENSITIVE (sensible a mayúsculas y minúsculas)
"""
