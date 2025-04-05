def sumar_tres(a,b,c):
    return a+b+c

if __name__ == "__main__":
    print("Calculadora de suma de 3 números:")
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))

    total = sumar_tres(num1,num2,num3)
    print(f"La suma de {num1}, {num2} y {num3} es: {total}")