
# ! -------------------------- COPIAR LISTAS --------------------------

a = [2,4,6,8,10]

# Diferentes formas de COPIAR una lista, para no modificar el array original
b = a[:] # ? es importante poner los [:] ya que se trata de una lista

c = a.copy() # ? método para copiar listas

d = list(a) # ? método constructor

print(f"Lista a: {a}")
print(f"Lista a: {b}")
print(f"Lista a: {c}")
print(f"Lista a: {d}")

# ! -------------NO SE PUEDE HACER---------------
# e = a  # ! NO COPIA LA LISTA, llama al array de dos formas iguales (crea otra referencia del array original)
original = ["pera", "manzana"]
print(f"Lista original: {original}")
copia = original  # ? ahora la lista tiene dos nombres
copia[0] = "camión"
print(f"modificando solo copia, copia = {copia} y original = {original}") # ! se han modificado las dos


# ! ------------ FORMAS DE BORRAR LISTAS --------------

# borro la lista incluyendo la variable
del a # ? borra tanto EL CONTENIDO como la PROPIA VARIABLE (la lista en sí)

# borro el contenido de la variable, los elementos
b.clear()
print(f"La lista b ahora está vacía: {b}")

# otra forma de eliminar los elementos de la lista, sobreescribiendo los valores de entro por "nada"
c[:] = [] # ? importante los dos puntos, "desde el principio hasta el final, vacíalo"
# c = [] como el anterior pero sin slicing, aquí en lugar de cambiar los elementos, revaloramos c como lista vacía
print(f"La lista c ahora está vacía: {c}")