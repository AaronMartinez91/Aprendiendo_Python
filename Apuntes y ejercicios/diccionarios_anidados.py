
#! Un diccionario anidado es un diccionario dentro de otro diccionario

print("--------------- DICCIONARIO ANIDADO ---------------")

universidad = {
    "nombre" : "iFP",
    "estudiantes" : {
        "Carlos": {
            "ref": "CA2345",
            "edad": 24,
            "estudios": "DAM 1",
            "hobbies": ["nadar", "dormir", "leer"]
        },
        "María": {
            "ref": "CA2388",
            "edad": 64,
            "estudios": "DAM 2",
            "hobbies": ["pintar", "hacer yoga", "salir de fiesta"]
        }
    }
}

#! ¿Qué estudios tiene Carlos?
print("Estudios de Carlos:  ", universidad["estudiantes"]["Carlos"]["estudios"])

#! El segundo hobby de Carlos
print("El segundo hobby de Carlos:", universidad["estudiantes"]["Carlos"]["hobbies"][1])

#! El último hobby de María
print("El último hobby de María:", universidad["estudiantes"]["María"]["hobbies"][-1])

#! Cómo puedo recorrer un diccionario anindado?
print("\nRecorrer un diccionario anidado")
for estudiante, info in universidad["estudiantes"].items():
    print (f"\nEstudiante: {estudiante}")
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
