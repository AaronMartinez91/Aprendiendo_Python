a, b = "Patrick", "Hetero"

# Operador de igualdad
resultado = a == b

print(f"Resultado de {a}=={b} es {resultado}")

# resultado = a = b
# print(f"Resultado de {a}=={b} es {resultado}") # Sobreescribe y de izquierda a derecha, la última que asigna es b

# Operador de comparación
resultado = a!=b
print(f"Resultado de {a}!={b} es {resultado}")

# Operador menor o igual <=
c, d = 4, 5
resultado2 = c<=d
print(f"Resultado de {c}<={d} es {resultado2}")

# Operador mayor o igual >=
resultado2 = c>=d
print(f"Resultado de {c}>={d} es {resultado2}")

# Comparamos cadenas
texto1 = "a"
texto2 = "b"
resultado3 = texto1>texto2
resultado4 = texto2>texto1
print(f"Resultado de a > b es {resultado3}")
print(f"Resultado de b > a es {resultado4}") # como 'a' va antes que 'b' es más 'pequeña'