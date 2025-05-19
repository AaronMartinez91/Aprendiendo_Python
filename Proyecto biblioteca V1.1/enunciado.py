"""
AUTHOR: Willoom
DATE: 12 May 2025
UPDATE: 15 May 2025

Este enunciado utiliza las librerías que se han de desarrollar para el proyecto Biblioteca.

No hay que diseñar una interfaz de usuario, sólo las librerías, clases, funciones, atributos 
y comportamiento especificado en el documento descriptivo del proyecto.

Este script asume que partimos de una base de datos vacía.
Si quieres usar la librería para gestionar una biblioteca real habría que crear un cargar_libros() 
en la clase Biblioteca, para invocarlo durante la construcción del objeto de clase Biblioteca.  

"""

from clase_biblioteca import Biblioteca
from clase_lector import Lector
from clase_libro import Libro
from clase_almacenado import LibroAlmacenado
from clase_prestado import LibroPrestado
from clase_incunable import LibroIncunable

"""
Definimos pasillos y subsecciones de la biblioteca
"""
FANTASIA = 1
FANTASIA_INFANTIL = 1
NOVELA = 2
NOVELA_MEDIEVAL = 1
    

"""
Creamos algunos libros almacenados e incunables.
Sólo están en memoria al principio.
"""
libro_nes = LibroIncunable("9780385176224","Never Ending Story", "Michael Ende", FANTASIA, FANTASIA_INFANTIL)
libro_m = LibroAlmacenado("9788418850837","Murtagh", "Christopher Paolini", FANTASIA, FANTASIA_INFANTIL)
libro_eq = LibroAlmacenado("9788481093353","El Quijote", "Miguel de Cervantes Saavedra", NOVELA, NOVELA_MEDIEVAL)
libro_tlb = LibroAlmacenado("9788420639901", "Tirant Lo Blanch", "Joanot Martorell", NOVELA, NOVELA_MEDIEVAL)   


"""
Creamos algunos lectores.
"""
# Bástian es un lector que siempre devuelve tarde los libros.
bastian = Lector("44444444X","Bástian", "Baltasar", "Bux")
# Se enganchó a un libro y tiene una penalización hasta el 5 de enero del año 2035
bastian.fecha_posible_para_préstamo = "05012035" 

# Hermione siempre intenta llevarse más de un libro a la vez.
hermione = Lector("55555555Y", "Hermione", "Granger", "Weasly")

# Augusto Odone es un hombre sencillo que trata de comprender cosas complejas,
# sacando un libro cada vez.
augusto = Lector("66666666Z", "Augusto", "Odone", "Murphy")



"""
El objeto biblioteca será el encargado de la gestión con 
la base de datos de Libros y Lectores.

Recuerda que aunque tengamos todos los datos de los libros en la misma tabla, se usarán unos 
u otros según la clase a la que pertenezca el objeto.
"""
biblioteca = Biblioteca('biblioteca.db', 'diario.txt')

biblioteca.libros = dict() # Por si olvidáis en el constructor poner un diccionario 

libros_nuevos = [libro_nes, libro_m, libro_eq, libro_tlb]

# Almacenamos en base de datos los libros.
for libro in libros_nuevos:
    biblioteca.adquirir_nuevo_libro(libro)
    
# Almacenamos en base de datos los lectores.
biblioteca.registrar_nuevo_lector(bastian)
biblioteca.registrar_nuevo_lector(hermione)
biblioteca.registrar_nuevo_lector(augusto)

"""
CASOS DE USO
"""

# Bástian es un chico que tiene penalización y que quiere retirar un incunable.
biblioteca.prestar(libro_nes, bastian)

# Hermione sacará un libro y tratará de llevarse otro, sin devolver el primero.
biblioteca.prestar(libro_tlb, hermione)
biblioteca.prestar(libro_eq, hermione)

# Augusto sacará un libro, lo leerá en el día y sacará otro.
biblioteca.prestar(libro_m, augusto)
biblioteca.recibir(libro_m.isbn, augusto)
biblioteca.prestar(libro_eq, augusto)




