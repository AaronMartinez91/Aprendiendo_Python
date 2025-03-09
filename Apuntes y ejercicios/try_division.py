# Pedir al usuario dos números y que nuestro programa haga la división


try:
    valor1 = float(input("Introduce el primer número: "))
    valor2 = float(input("Introduce el segundo número: "))

    print(f"El resultado entre dividir {valor1} entre {valor2} es {valor1/valor2}.")
except ZeroDivisionError:
    print("❌ ¡Error! No se puede dividir entre 0")
except ValueError:
    print("❌ ¡Error! Debes introducir dos números")
      