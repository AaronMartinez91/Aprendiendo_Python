from clase_almacenado import LibroAlmacenado


class LibroIncunable(LibroAlmacenado):  
    def __init__(self, isbn, titulo, autor, categoria, subcategoria):
        super().__init__(isbn, titulo, autor, categoria, subcategoria)

    def asignar_lector(self, l):
        return False # este NUNCA podrá ser asignado
