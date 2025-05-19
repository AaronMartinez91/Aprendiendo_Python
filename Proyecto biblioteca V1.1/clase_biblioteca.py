import sqlite3  # primero de todo importo sqlite3 para poder usarlo
# importo las clases para trabajar con ellas
from clase_lector import Lector
from clase_almacenado import LibroAlmacenado
from clase_incunable import LibroIncunable
from clase_prestado import LibroPrestado
from clase_libro import Libro
from datetime import date, timedelta, datetime


class Biblioteca:
    
    DATABASE = 'biblioteca.db' # en este caso uso una constante para almacenar el nombre de la base de datos para dar integridad, así si tengo que hacer modificaciones solo tengo que cambiar aquí
    DIARIO = 'diario.txt' # lo mismo pero con el diario

    def __init__(self, database=None, diario=None): # estos dos None son por lo que comento más abajo
        
        """si no he entendido mal el enunciado, debía crear las dos constantes anteriores. Sin embargo, en enunciado.py se llama así: "biblioteca = Biblioteca('biblioteca.db', 'diario.txt')"
        por lo que estaba teniendo errores. Por eso mismo añado el siguiente trozo de código que literalmente, si se pasan parámetros los usará, de lo contrario usará los que tiene por defecto.
        """
        if database:
            self.DATABASE = database
        if diario:
            self.DIARIO = diario

        # esto inicializa la base de datos si no existe
        self.con = sqlite3.connect(self.DATABASE)  # creo la variable con que conecta a la base de datos
        self.cursor = self.con.cursor() # lo mismo con el cursor
        self.crear_tablas() # también llamamos siempre a la función que crea las tabla si no existen, así siempre que se use esta clase existirá dicha tabla
        self.libros = {} # aquí almaceno los distintos libros en forma de diccionario

    def crear_tablas(self):
        # esta función crea las tabla SI NO EXISTEN
        self.cursor.execute("CREATE TABLE IF NOT EXISTS libros (isbn TEXT PRIMARY KEY, titulo TEXT NOT NULL, autor TEXT NOT NULL, dni_lector TEXT, categoria INTEGER, subcategoria INTEGER, fecha_prestamo TEXT, estado TEXT CHECK(estado IN ('almacenado', 'prestado', 'incunable')))") # respecto al tipo de dato del atributo "tipo", pretendía usar un ENUM, pero aparentemente SQLITE no lo permite y esta es la forma de poder controlar directamente que solo se le puedan introducir esos 3 posibles resultados
        self.con.commit()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS lectores (dni TEXT PRIMARY KEY, nombre TEXT NOT NULL, apellido1 TEXT NOT NULL, apellido2 TEXT, fecha_para_prestamo TEXT NOT NULL)") 
        self.con.commit()

    # función que abre diario.txt y añade al final del archivo un nuevo registro con salto de línea
    def registrar_en_diario(self, mensaje):
        with open(self.DIARIO, 'a', encoding='utf-8') as adicion_diario:  # abro con with para que se cierre automáticamente, 'a' para añadir al final, utf-8 para que entren caracteres especiales
            adicion_diario.write(mensaje + '\n')


    def prestar(self, libro, lector):
        # esta función intenta prestar un libro a un lector
       
        fecha_actual = date.today().strftime("%d%m%Y")  # necesito una variable para almacenar la fecha en la que ocurre todo lo que voy a registrar
        mensaje_base = f"-{date.today().strftime('%d/%m/%Y')} {datetime.now().strftime('%H:%M')}: " # con esto estandarizo el inicio de todos los mensajes con la fecha transformada en STR y :, para registrar correctamente todo lo que pasa

        # voy a hacer varias verificaciones antes de saber si puedo prestar el libro. Todas son "if", puesto que puede haber varios motivos a la vez por los que no se pueda prestar y todos deben quedar registrados

        # primero compruebo si el libro es un incunable
        if isinstance(libro, LibroIncunable):
            mensaje = mensaje_base + f"{lector.nombre} {lector.apellido1} {lector.apellido2} jamás podrá sacar {libro.titulo} porque es un incunable."
            self.registrar_en_diario(mensaje)
            return False

        # Después me aseguro de que el lector en cuestión no tenga penalización
        if lector.fecha_posible_para_préstamo > fecha_actual:
            # Calculo los días de penalización que tiene (debo tenerlo todo en formato DDMMAA, pillo el trozo que necesito del string, lo transformo a INT y luego a date y calculo para sacar los días)
            dias_penalizacion = (date(int(lector.fecha_posible_para_préstamo[4:8]), int(lector.fecha_posible_para_préstamo[2:4]), int(lector.fecha_posible_para_préstamo[:2])) - date.today()).days
            mensaje = mensaje_base + f"NO se presta el libro {libro.titulo} a {lector.nombre} {lector.apellido1} {lector.apellido2} porque le quedan {dias_penalizacion} días de penalización."
            self.registrar_en_diario(mensaje)
            return False
        
        # compruebo que el lector no tenga ya un libro prestado
        self.cursor.execute(f"SELECT isbn FROM libros WHERE dni_lector = '{lector.dni}' AND estado = 'prestado'")
        libro_prestado = self.cursor.fetchone()
        if libro_prestado:
            mensaje = mensaje_base + f"{lector.nombre} {lector.apellido1} {lector.apellido2} no puede sacar el libro '{libro.titulo}' porque ya tiene un libro prestado."
            self.registrar_en_diario(mensaje)
            return False
        
        # ahora solo me falta comprobar que el libro que estoy pidiendo no esté ya prestado
        self.cursor.execute(f"SELECT estado FROM libros WHERE isbn = '{libro.isbn}'")
        libro_ya_prestado = self.cursor.fetchone()
        if libro_ya_prestado[0] == 'prestado':
            mensaje = mensaje_base + f"El libro {libro.titulo} ya está prestado a otra persona."
            self.registrar_en_diario(mensaje)
            return False
        
        # Asigno el libro al lector
        fecha_retorno = (date.today() + timedelta(days=7)).strftime('%d%m%Y')
        self.cursor.execute(f"UPDATE libros SET dni_lector = '{lector.dni}', fecha_prestamo = '{fecha_retorno}', estado = 'prestado' WHERE isbn = '{libro.isbn}'")
        self.con.commit()
        
        # una vez he comprobado los posibles errores actualizo en memoria
        libro_prestado = LibroPrestado(libro.isbn, libro.titulo, libro.autor)
        libro_prestado.categoria = libro.categoria 
        libro_prestado.subcategoria = libro.subcategoria
        self.libros[libro.isbn] = libro_prestado

        # por último registro ese cambio
        mensaje = mensaje_base + f"Se presta el libro {libro.titulo} a {lector.nombre} {lector.apellido1} {lector.apellido2}."
        self.registrar_en_diario(mensaje)
        return True
    
    def recibir(self, isbn, lector): # el enunciado me exige llamarlo dni pero me estaba dando problemas porque en enunciado.py me envía el OBJETO ENTERO, NO EL DNI. así que le cambio el nombre
        # esta función establece el libro a disponible en estantería
        mensaje_base = f"-{date.today().strftime('%d/%m/%Y')} {datetime.now().strftime('%H:%M')}: "
        
        # una vez más todo "ifs" para registrar todos los posibles problemas
        # primero compruebo si el libro existe y es "prestado"
        self.cursor.execute(f"SELECT titulo, estado, fecha_prestamo FROM libros WHERE isbn = '{isbn}'")
        libro_info = self.cursor.fetchone()
        if not libro_info or libro_info[1] != 'prestado':
            mensaje = mensaje_base + f"Error: El libro con ISBN {isbn} no está prestado."
            self.registrar_en_diario(mensaje)
            return False
        
        titulo = libro_info[0]
        fecha_retorno = libro_info[2]
        
        # una vez más, cambiando los tipos de datos hago una resta simple para ver si hay o no días de retraso en la entrega al recibirlo
        fecha_ret = date(int(fecha_retorno[4:8]), int(fecha_retorno[2:4]), int(fecha_retorno[:2]))
        dias_retraso = (date.today() - fecha_ret).days
        
        # para la siguiente parte necesitaré mostrar el nombre del lector para mostrarlo en el mensaje, por lo que lo preparo aquí
        self.cursor.execute(f"SELECT nombre, apellido1, apellido2 FROM lectores WHERE dni = '{lector.dni}'")
        lector_info = self.cursor.fetchone()

        nombre_completo = f"{lector_info[0]} {lector_info[1]} {lector_info[2]}" if lector_info else lector.dni

        # en función de si hay o no días de retraso, registro que el libro se recibió bien o aplico penalización
        if dias_retraso <= 0:
            mensaje = mensaje_base + f"{nombre_completo} devuelve el libro {titulo} en fecha."
            self.registrar_en_diario(mensaje)
        else:
            dias_penalizacion = dias_retraso * 2
            nueva_fecha = (date.today() + timedelta(days=dias_penalizacion))
            nueva_fecha_str = nueva_fecha.strftime('%d%m%Y')
            
            self.cursor.execute(f"UPDATE lectores SET fecha_posible_para_prestamo = '{nueva_fecha_str}' WHERE dni = '{lector.dni}'")
            self.con.commit()
            
            mensaje = mensaje_base + f"{nombre_completo} devuelve tarde el libro {titulo} {dias_retraso} días.\n"
            mensaje += f"{nombre_completo} no podrá sacar libros hasta el {nueva_fecha.strftime('%d/%m/%Y')}."
            self.registrar_en_diario(mensaje)
        
        # Por último una vez más actualizo el estado del libro a almacenado
        self.cursor.execute(f"UPDATE libros SET estado = 'almacenado', dni_lector = NULL, fecha_prestamo = NULL WHERE isbn = '{isbn}'")
        self.con.commit()
        
        # Actualizo en memoria
        self.cursor.execute(f"SELECT autor, categoria, subcategoria FROM libros WHERE isbn = '{isbn}'")
        libro_data = self.cursor.fetchone()
        if libro_data:
            autor, categoria, subcategoria = libro_data
            libro_almacenado = LibroAlmacenado(isbn, titulo, autor, categoria, subcategoria)
            self.libros[isbn] = libro_almacenado
        
        return True

    def adquirir_nuevo_libro(self, libro):
        # este método me permite añadir nuevos libros al sistema, primero asegurándome de que no exista previamente
        if libro.isbn in self.libros:
            return False
        
        # lo añado al diccionario de la biblioteca     
        self.libros[libro.isbn] = libro
        
        # el libro será por defecto almacenado a menos que sea incunable
        tipo = 'incunable' if isinstance(libro, LibroIncunable) else 'almacenado'
        
        self.cursor.execute(f"INSERT INTO libros (isbn, titulo, autor, categoria, subcategoria, estado) VALUES ('{libro.isbn}', '{libro.titulo}', '{libro.autor}', {libro.categoria}, {libro.subcategoria}, '{tipo}')")
        self.con.commit()
        return True

    def registrar_nuevo_lector(self, lector):
        # método para registrar nuevos lectores
        try:
            self.cursor.execute(f"INSERT INTO lectores VALUES ('{lector.dni}', '{lector.nombre}', '{lector.apellido1}', '{lector.apellido2}', '{lector.fecha_posible_para_préstamo}')")
            self.con.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        
    def actualizar_libro(self, libro):
        # método para actualizar información de un libro que ya existe en la base de datos
        try:
            # primero verificamos que realmente exista
            self.cursor.execute(f"SELECT isbn FROM libros WHERE isbn = '{libro.isbn}'")
            if not self.cursor.fetchone():
                return False
            
            # en caso de que exista, modificamos los datos
            self.cursor.execute(f" UPDATE libros SET titulo = '{libro.titulo}', autor = '{libro.autor}', categoria = {libro.categoria}, subcategoria = {libro.subcategoria} WHERE isbn = '{libro.isbn}'")
            self.con.commit()
            return True
        except sqlite3.Error:
            return False
        
    def actualizar_lector(self, lector):
        # sigo con la misma lógica que actualizar_libro
        try:
            # primero verifico
            self.cursor.execute(f"SELECT dni FROM lectores WHERE dni = '{lector.dni}'")
            if not self.cursor.fetchone():
                return False
            
            # luego modifico
            self.cursor.execute(f"UPDATE lectores SET nombre = '{lector.nombre}', apellido1 = '{lector.apellido1}', apellido2 = '{lector.apellido2}', fecha_posible_para_prestamo = '{lector.fecha_posible_para_prestamo}' WHERE dni = '{lector.dni}'")
            self.con.commit()
            return True
        except sqlite3.Error:
            return False