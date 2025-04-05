import suma # importo el módulo suma entero


print("Introduce 3 números: ")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

total = suma.sumar_tres(num1,num2,num3)
print (f"La suma de {num1} + {num2} + {num3} = {total}")