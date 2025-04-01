
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

# # Crear una función que retorne una lista con solo los números pares de la lista original.

# def filtrar_pares(lista):

  







# print(filtrar_pares(lista)) 

















# #! Ejercicio 3:

# # Crear una función que elimine los elementos duplicados de la lista, manteniendo el orden original.



# def eliminar_duplicados(lista):

  







# lista = [3, 4, 8, 9, 4, 7, 3, 3,3 ]

# print (f"Lista original: {lista}")

# print(f"Lista sin repetidos: {eliminar_duplicados(lista)}")













# #! Ejercicio 4:



# # Crear una función que cuente cuántos elementos son mayores que un valor dado.









# lista = [3, 4, 8, 9, 4, 7]

# print(contar_mayores_que(lista, 5)) 

















# #! Ejercicio 5: 

# # Crear una función que retorne el índice de la primera ocurrencia de un elemento, o -1 si no existe



# def encontrar_indice(lista, elemento):

  





# lista = [3, 4, 8, 9, 4, 7]

# print(encontrar_indice(lista, 9)) 















# #! Ejercicio 6:

# # Crear una función que genere una nueva lista con el cuadrado de cada elemento.





# def cuadrados(lista):

  





# lista = [3, 4, 8, 9, 4, 7]

# print(cuadrados(lista)) 















# #! Ejercicio 7:



# # Crear la función 'promedio' que acceptará una lista y devolverá el valor promedio de esa lista con 3 decimales

# # NO se puede utilizar el método sum()



# def promedio(lista):

  



  

#   return



# lista = [3, 4, 8, 9, 4, 7]

# print(f"El promedio es:")















# #! Ejercicio 8:



# # Crear una función que retorne un diccionario con la frecuencia (cuántas veces ha salido) de cada elemento.

# def frecuencia_elementos(lista):

  





# # Ejemplo:

# lista = [3, 4, 8, 9, 4, 7]

# print(frecuencia_elementos(lista)) # Salida: {3:1, 4:2, 8:1, 9:1, 7:1}















# #! Ejercicio 9: Filtra elementos que son múltiplos de dos divisores diferentes



# def filtrar_multiplos(lista, divisor1, divisor2):

  





# lista = [10, 15, 20, 5, 3, 35, 40,50]

# print (f"De la lista {lista}")

# print("Los múltiplos de 2 y 5 son: ", filtrar_multiplos(lista, 2, 5)) 