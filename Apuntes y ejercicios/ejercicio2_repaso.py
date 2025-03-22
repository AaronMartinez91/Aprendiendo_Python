"""
Imprimir los números del 1 al 20
Para números divisibles por 3, imprimir la palabra "Fizz"
Para números divisibles por 5, imprimir "Buzz"
Para números divisibles por 3 y 5, imprimir "FizzBuzz"
En cualquier otro caso, imprimir el número
"""

for i in range (1,21):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 !=0 and i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)