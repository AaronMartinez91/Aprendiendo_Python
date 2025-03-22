"""
Suma los números del 25 al 0 (ambos incluidos) en orden descendente
"""

total = 0
for i in range (25, -1, -1):   
    # total = total + i
    total += i

print(f"La suma total de los números del 25 al 0 en orden descendente es igual a {total}")