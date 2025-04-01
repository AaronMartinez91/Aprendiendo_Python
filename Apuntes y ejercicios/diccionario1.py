
#! Ejercicio: crear un diccionario llamado estudiante con 3 llaves: nombre, edad y estudios. Imprime el diccionario
estudiante = {
    'nombre': 'Aarón',
    'edad': 33,
    'estudios': 'DAM'
}

#? varias formas de imprimir el diccionario
print(estudiante)

for llave, valor in estudiante.items():
    print(f"{llave}: {valor}")

for llave in estudiante:
    print(f"{llave} -> {estudiante[llave]}")

#! otra forma de crear un diccionario usando el "constructor" dict()

otra_forma = dict(nombre="Patrick", edad="19", sexo="ERROR 404")
print(otra_forma)

#! Encontrar la longitud del diccionario (cuántas llaves-valores tiene)
print(f"La longitud del diccionario es: {len(estudiante)}")

#? Encontrar la longitud de otra forma
longitud = 0
for llave in estudiante.keys():
    longitud += 1
print(f"La longitud de {estudiante} es {longitud}")

#! Verificar si existe una llave en un diccionario
if "edad" in estudiante:
    print("Tiene edad registrada.")
else:
    print("No tiene edad registrada.")

#! modifica el diccionario "estudiante", añadiendo 3 pares llave/valor nuevas
estudiante['teléfono'] = '666 666 666'
estudiante['isRepetidor'] = "No"
estudiante['Ciudad'] = "L\'Hospitalet de LLobregat"
estudiante['CP'] = "08901"

print(f"Imprimimos nuevo diccionario: {estudiante}")

#! Obtener listado de las llaves (2 formas!)
for llave in estudiante.keys():
    print(llave)

print(f"Otra forma de obtener las llaves: {estudiante.keys()}") #? mismo método sin el for

#! Obtener listado de los valores (2 formas!)
for valor in estudiante.values():
    print(valor)

print(f"Otra forma de obtener los valores: {estudiante.values()}") #? mismo método sin el for


#! Obtener listado de las llaves-valores (2 formas!)
for llave, valor in estudiante.items():
    print(f"{llave} : {valor}")

print(f"Otra forma de obtener las llaves y los valores: {estudiante.items()}")

#! Eliminar la llave cp
del estudiante['CP']

print(f"Diccionario eliminando el CP: {estudiante}")

#! Limpiar un diccionario (vaciarlo o eliminarlo)

print("Antes de borrar el diccionario: ")
print(estudiante)
print("Después de borrar el diccionario: ")
estudiante.clear() #? Lo vacía
print(estudiante)
del estudiante #? elimina la variable por completo
print(estudiante)
