from clase_libro import Libro
import sqlite3
from clase_lector import Lector

class LibroPrestado(Libro):
    def __init__(self, isbn, titulo, autor):
        super().__init__(isbn, titulo, autor) # una vez más, con esto recibo los atributos de superclase Libro
        self.categoria = None
        self.subcategoria = None

    def consultar_lector(self):
        # consulto por isbn a la base de datos y devuelvo el objeto del lector al que está asociado
        try:
            DATABASE = 'biblioteca.db'
            con = sqlite3.connect(DATABASE)
            cursor = con.cursor()
            
            cursor.execute(f"SELECT dni_lector FROM libros WHERE isbn = '{self.isbn}'")
            resultado = cursor.fetchone()

            if not resultado or not resultado[0]:
                return None  # En este caso devolvemos None si no hay lector asignado al libro encuestión, ya que el mensaje de que no tiene asignado lo mostraremos en la clase Biblioteca cuando esta función devuelva None
            
            # como el enunciado nos pide que devolvamos un objeto lector, vamos a consultar a la base de datos el lector que tiene este dni y a crearlo desde ahí
            dni_lector = resultado[0]

            cursor.execute(f"SELECT nombre, apellido1, apellido2, fecha_posible_para_prestamo FROM lectores WHERE dni = '{dni_lector}'")
            datos_lector = cursor.fetchone()
            
            if not datos_lector: # si no existen datos de este supuesto lector (podríamos haber hecho mal algo previamente) devovlemos None otra vez
                return None
            
            # he importado la clase Lector para poder crear este objeto y así devolverlo
            lector = Lector(
            dni=dni_lector,
            nombre=datos_lector[0],
            apellido1=datos_lector[1],
            apellido2=datos_lector[2]
        )
            # establezco la fecha de préstamo posible
            lector.fecha_posible_para_préstamo = datos_lector[3]
            
            return lector
            
        except sqlite3.Error as error:
            print(f"Error en consultar_lector: {error}")
            return None
        finally:
            con.close()    
            
       
    
    def consultar_retorno(self):
        # sigo el mismo proceso que hasta ahora para conectarme con la base de datos y hago una consulta simple que me devuelve la fecha
        try:
            DATABASE = 'biblioteca.db'
            con = sqlite3.connect(DATABASE)
            cursor = con.cursor()
            
            
            cursor.execute(f"SELECT fecha_retorno FROM libros WHERE isbn = '{self.isbn}'")
            
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                return None
            
        except sqlite3.Error as error:
            print(f"Error al consultar fecha retorno: {error}")
            return None
        finally:
            con.close()
