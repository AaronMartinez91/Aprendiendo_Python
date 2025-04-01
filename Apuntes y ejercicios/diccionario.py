print("-"*15, "DICCIONARIOS", "-"*15)

#! creamos un diccionario de persona: clave y un valor
persona = {
    'nombre': 'Encarni',
    'edad': 99,
    'ciudad': 'L\'Hospitalet'
}

#! imprimimos el diccionario:
print(f"Diccionario de persona: {persona}")

#! accedeomos a los elementos del diccionario:
print(f"Nombre: {persona['nombre']}") #? accedo al contenido de la parte 'nombre', como es un diccionario el [0] no funciona
print(f"Edad: {persona.get('edad')} años.") #? el método get me permite acceder también
print(f"Vive en: {persona.get('ciudad')}") #? mismo método

#! modificamos los elementos del diccionario

persona['edad'] = 39

print(f"Diccionario de persona cambiando la edad: {persona}")

#! agregar un nuevo elemento al diccionario
persona['profesión'] = 'Programadora'
print(f"Diccionario de persona añadiendo la profesión: {persona}")

#! eliminar un elemento 
del persona['ciudad']
print(f"Diccionario de persona eliminando la ciudad: {persona}")

profesion = persona.pop('profesión') #? pop también elimina, pero permite guardar lo eliminado en una variable (opcional) antes de hacerlo
print(f"Diccionario de persona eliminando la profesión: {persona}")

#! recorrer los elementos de un diccionario (llave, valor)
for llave, valor in persona.items(): #? es importante el items para poder acceder a las dos
    print(f"Llave: {llave}, valor: {valor}")

#! obtener solo las llaves
print("\nLas llaves del diccionario: ")
for llave in persona.keys():
    print(f"LLave: {llave}")


#! obtener solo los valores
print("\nValores del diccionario: ")
for valor in persona.values():
    print(f"Valor: {valor}")
