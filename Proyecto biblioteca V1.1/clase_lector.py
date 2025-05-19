from datetime import date


class Lector:
    def __init__(self, dni, nombre, apellido1, apellido2):
        self.dni =dni  
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        
        # necesitamos establecer la fecha al día anterior a la creación del Lector según el enunciado. Para ello uso un par de variables 
        hoy = date.today()
        ayer = hoy.replace(day = hoy.day - 1) # el método replace me permite restarle un día al día actual
        self.fecha_posible_para_préstamo = ayer.strftime('%d%m%Y') # es importante que cambie el formato de fecha a 'DDMMAAAA' para trabajar con él correctamente en enunciado.py