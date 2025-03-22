
# ! AGREGAR ELEMENTOS A UNA LISTA

lista = [1, 2, 3, 4, 5]
print(f"Lista original: {lista}")

# ? Puedo modificar los elementos de la lista (es mutable)

lista[0] = 10
print(f"Lista modificada: {lista}")

# ! Agregar SOLO UN nuevo elemento AL FINAL de la lista:     .append()
lista.append(6)
print(f"Lista modificada con un elemento añadido al final: {lista}")

# ! Agregar VARIOS elementos AL FINAL de la lista:    .extend()
lista.extend([7,8,9])
print(f"Lista modificada con varios elementos añadidos al final: {lista}")

# ! También puedo utilizar el operador + (concatenación)
lista = lista + [10,11,12] # ? Si pongo los valores al principio los añade al principio: [10,11,12] + lista
print(f"Lista modificada con varios elementos añadidos al final: {lista}")

# ! Agregar un elemento en un índice específico (donde yo quiera)    .insert()
lista.insert(2, 999) # ? En la posición 2, introduce el valor 999
print(f"Lista modificada con varios elementos añadidos en un índice específico: {lista}")

# usamos otra lista distinta para ver como añadiríamos varios
frutas = ['manzana', 'plátano', 'naranja']
elementos_a_insertar = ['rueda', 'llave']
posicion = 1
print(f"La lista sin modificar: {frutas}")

for elemento in elementos_a_insertar[::-1]:     # ? debes invertirlo para que al introducir uno a uno no los vaya desplazando a la derecha
    frutas.insert(posicion, elemento)
print(f"La lista con elementos introducidos: {frutas}")

