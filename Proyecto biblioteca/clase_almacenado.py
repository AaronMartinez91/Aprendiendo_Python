from clase_libro import Libro
from datetime import date, timedelta
import sqlite3

class LibroAlmacenado(Libro):
    def __init__(self, isbn, titulo, autor, categoria, subcategoria):
        super().__init__(isbn, titulo, autor) # tal y como dice el enunciado, redefino el constructor para recibir los atributos de la superclase Libro, y poder crear así el objeto con todos los atributos
        self.categoria = categoria 
        self.subcategoria = subcategoria

    def ubicación(self):
        ubicacion = (f"{self.categoria}.{self.subcategoria}")
        return ubicacion
    
    def asignar_lector(self, l):
        try:
            DATABASE = 'biblioteca.db' # sigo con la consistencia de clase_biblioteca, puesto que voy a hacer modificaciones en la base de datos vuelvo a generar la conexión
            con = sqlite3.connect(DATABASE)
            cursor = con.cursor()
            
            # primero verifico si el libro ya está prestado o no
            cursor.execute(f"SELECT estado FROM libros WHERE isbn = '{self.isbn}'")
            estado = cursor.fetchone()
            if estado and estado[0] == 'prestado':
                return False

            fecha_retorno = (date.today() + timedelta(days=7)).strftime('%d%m%Y') # al igual que en la clase lector, controlo la diferencia de tipo de dato de python vs SQL
            
            # actualizo los valores en la base de datos
            cursor.execute(f"UPDATE libros SET dni_lector = '{l.dni}', fecha_retorno = '{fecha_retorno}', estado = 'prestado' WHERE isbn = '{self.isbn}'")
            con.commit()
            return True
        
        except sqlite3.Error:
            return False  # devuelve un booleano false si por algún motivo no no puede prestarse el libro al lector
        finally:
            con.close()