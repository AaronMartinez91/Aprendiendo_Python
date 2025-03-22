print("BREAK")
for numero in range(1,10):
    if(numero%2==0):
        print(numero)
        break         # el break rompe el bucle


print("Adiós")

for numero in range(1,10):
    if(numero%2==1):
        continue      # está ignorando los números impares por el continue, pero como el print está al final está imprimiendo todos los números (excepto los previamnete ignorados)
    print(numero)
        