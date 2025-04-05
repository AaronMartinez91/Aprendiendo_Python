
#! FUNCIONES LAMBDA: son funciones ANÓNIMAS que se definen EN UNA SOLA LÍNEA, se usan para tareas simples

suma = lambda a,b: a + b

print(suma(2,3))

#! Función lambda que multiplique 3 números
multiplica_3_num = lambda a,b,c: a*b*c

print(multiplica_3_num(1,2,3))

#! Dada la siguiente lista, función lambda que filtra los números pares
numeros = [1,2,3,4,5,6,7,8,9,10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# método tradicional (sin lambda)
pares = []
for x in numeros:
    if x % 2 == 0:
        pares.append(x)

#! Función lambda para ver si es mayor de edad o no
es_mayor = lambda edad: "Mayor de edad" if edad >= 18 else "Menor de edad"

print(es_mayor(14))
print(es_mayor(77))

#! función map: para cada elemento de la lista tienes que hacer algo

numeros = [1,2,3,4,5,6]
dobles = list (map(lambda x : x*2,numeros))
print(f"{numeros}\n{dobles}")

# Equivalente tradicional:
dobles = []
for x in numeros:
    dobles.append(x*2)