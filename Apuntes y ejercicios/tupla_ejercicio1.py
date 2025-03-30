
# Crear una tupla con los números del 20 al 30, mostrar la longitud de la tupla y el último elemento
lista = []
for i in range(20,31):
    lista.append(i)

tupla = tuple(lista)

print(f"Tupla: {tupla}, longitud: {len(tupla)}, último elemento: {tupla[-1]} o {tupla[len(tupla)-1]} o {tupla[-1:][0]}") #! la tercera forma pilla toda la tupla invertida y pilla el primer elemento de esta

# ? otra forma con funciones:
n = list(range(20,31))
m = tuple(n)
print(m)
    
# Crear una función que reciba una tupla y devuelva la SUMA de sus elementos
def suma_elementos(tupla):
    suma = 0
    for numero in tupla:
        suma += numero
    return(suma)

print(f"La suma de los elementos de la tupla {tupla} es: {suma_elementos(tupla)}")

# ? con la función sum
suma2 = sum(tupla)
print(suma2)

# Convierte una lista de nombres en una tupla y muestra el último elemento

lista2 = ["Alejandro", "Patrick", "Hugo", "Sergio"]

tupla2 = tuple(lista2)

print(f"El último elemento de la tupla {type(tupla2)}:{tupla2} es {tupla2[-1]}")