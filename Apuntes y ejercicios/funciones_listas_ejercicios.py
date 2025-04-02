
#! Ejercicio 1:

# Crea una función que retorne el máximo y el mínimo de una lista

def maximo_y_minimo(lista):
    maximo = float('-inf') #? defino maximo como el valor más bajo posible para que el siguiente siempre sea más alto (lo necesito para la primera vez que lo comparo)
    minimo = float('+inf')
    for elemento in lista:
       if maximo < elemento:    
        maximo = elemento
       if minimo > elemento: #? en este caso son dos "if" ya que en el mismo bucle quiero que me haga las dos cosas
        minimo = elemento
    return maximo,minimo

lista = [3, 4, 8, 9, 4, 7]

resultado = maximo_y_minimo(lista)

if resultado:

  maximo, minimo = resultado

  print(f"Máximo: {maximo}, Mínimo: {minimo}") # Salida: Máximo: 9, Mínimo: 3
else:

  print("La lista está vacía")


# #! Ejercicio 2:

# Crear una función que retorne una lista con solo los números pares de la lista original.

def filtrar_pares(lista):
  lista_pares = []
  for numero in lista:
    if numero % 2 == 0:
      lista_pares.append(numero)
  return lista_pares
  

print(filtrar_pares(lista)) 


#! Ejercicio 3:

# Crear una función que elimine los elementos duplicados de la lista, manteniendo el orden original.
lista = [3, 4, 8, 9, 4, 7, 3, 3, 3]

def eliminar_duplicados(lista):
  lista_sin_duplicados = []
  for numero in lista:
    if numero not in lista_sin_duplicados:  #! inicialmente pensé en usar la propia lista y eliminar con el método remove, pero al estar iterando sobre una lista que modifico se volvía loco y me borraba cosas que no tocaban
      lista_sin_duplicados.append(numero)
  return lista_sin_duplicados


print (f"Lista original: {lista}")

print(f"Lista sin repetidos: {eliminar_duplicados(lista)}")



#! Ejercicio 4:

# Crear una función que cuente cuántos elementos son mayores que un valor dado.

lista = [3, 4, 8, 9, 4, 7]

def contar_mayores_que(lista, valor_dado):
  mayores = 0
  for valor in lista:
    if valor > valor_dado:
      mayores += 1
  return mayores

print(contar_mayores_que(lista, 5)) 


#! Ejercicio 5: 

# Crear una función que retorne el índice de la primera ocurrencia de un elemento, o -1 si no existe


lista = [3, 4, 8, 9, 4, 7]

def encontrar_indice(lista, elemento):
  for i in range (len(lista)): #! itero en función de la longitud de la lista
    if lista[i] == elemento:   #! comparo el valor en el rango de i con el valor del elemento
      return i                 #! si coinciden, devuelvo el valor del índice
  return -1
    
print(encontrar_indice(lista, 9)) 



#! Ejercicio 6:

# Crear una función que genere una nueva lista con el cuadrado de cada elemento.

lista = [3, 4, 8, 9, 4, 7]

def cuadrados(lista):
  lista_cuadrados = []
  for valor in lista:
    lista_cuadrados.append(valor**2)
  return lista_cuadrados

print(cuadrados(lista)) 


#! Ejercicio 7:

# Crear la función 'promedio' que acceptará una lista y devolverá el valor promedio de esa lista con 3 decimales

# NO se puede utilizar el método sum()


lista = [3, 4, 8, 9, 4, 7]

def promedio(lista):
  if len(lista) == 0:
    return "La lista está vacía" #? evito posibles divisiones entre 0
  else:
    suma_total = 0
    for valor in lista:
      suma_total += valor
    return suma_total/(len(lista))


print(f"El promedio es: {promedio(lista):.3f}")


#! Ejercicio 8:

# Crear una función que retorne un diccionario con la frecuencia (cuántas veces ha salido) de cada elemento.

lista = [3, 4, 8, 9, 4, 7]

def frecuencia_elementos(lista):
  diccionario_frecuencia = {}  #! creo el diccionario vacío
  for elemento in lista:    
    if elemento in diccionario_frecuencia:       #! por cada elemento dentro de la lista, compruebo si está dentro, si lo está, le sumo 1 a la cantidad, si no lo está, le pongo el primer valor (1)
      diccionario_frecuencia[elemento] += 1
    else:
      diccionario_frecuencia[elemento] = 1
  return diccionario_frecuencia

# Ejemplo:


print(frecuencia_elementos(lista)) # Salida: {3:1, 4:2, 8:1, 9:1, 7:1}



#! Ejercicio 9: Filtra elementos que son múltiplos de dos divisores diferentes

lista = [10, 15, 20, 5, 3, 35, 40,50]

def filtrar_multiplos(lista, divisor1, divisor2):
  lista_multiplos = []
  for numero in lista:
    if numero % divisor1 == 0 and numero % divisor2 == 0:  #! con este filtro me aseguro de que son divisibles por AMBOS divisores A LA VEZ
      lista_multiplos.append(numero)
  return lista_multiplos


print (f"De la lista {lista}")

print("Los múltiplos de 2 y 5 son: ", filtrar_multiplos(lista, 2, 5)) 