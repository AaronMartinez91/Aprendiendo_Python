
#! Una función puede devolver VARIOS RESULTADOS

def persona_mayusculas(nombre, apellido, edad):
    print("Esta función devuelve VARIOS VALORES (tupla)")
    return nombre.upper(),apellido.upper(),edad

nombre,apellido,edad = persona_mayusculas("Aarón","Martínez",99)
print(f"Resultado -> Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}")

#! Se pueden asignar valores PREDETERMINADOS a los parámetros

def saludar_persona(nombre="Anónimo"):
    print(f"Bienvenido, {nombre}")

saludar_persona("Pepe Luís")
saludar_persona() #! como he predeterminado el parámetro, puedo invocarla sin argumento, y esta introducirá automáticamente el predeterminado

#! FUNCIÓN CON ARGUMENTOS POR NOMBRE

def imprimir_persona(nombre="Jorse Luís", apellido="Trucutrú", edad=100):
    print(f"Persona: nombre = {nombre}, apellido = {apellido}, edad={edad}")

imprimir_persona()
imprimir_persona(nombre="Carlos")
imprimir_persona(nombre="Carlos", apellido="Goicoetxea")
imprimir_persona(nombre="Carlos", apellido="Goicoetxea", edad = 2)

#! FUNCIONES CON NÚMERO VARIABLE DE ARGUMENTOS (*args)

def suma_total(*numeros):
    return sum(numeros)

print(suma_total())
print(suma_total(2))
print(suma_total(2,3))
print(suma_total(2,3,4,5,6))
print(suma_total(2,2,3,4,5,6,7,7,8))

#! Funciones con argumentos clase (**kwargs), permite pasar MÚLTIPLES valores con nombre sin necesidad de definir varios parámetros

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f" {clave} -> {valor}", end=" ")
    print("-----------------")

mostrar_info(nombre="Pepe", edad=99, ciudad="Barcelona")
mostrar_info(nombre="Sandra", edad=19, ciudad="L'Hospitalet", en_activo="Sí", CP="08034")