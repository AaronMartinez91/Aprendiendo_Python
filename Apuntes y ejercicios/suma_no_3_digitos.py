"""
Ejercicio: Escribe un programa que dado un número de 3 dígitos nos de la suma de sus dígitos.
No vale utilizar ninguna función que me ayude al cálculo
"""

while True:
    try:
        numero_inicial = int(input("Introduce un número de 3 dígitos: "))
        if 100 <= numero_inicial <= 999:
            primer_numero = numero_inicial//100  
            segundo_numero = (numero_inicial - (primer_numero*100))//10 # segundo_numero = (numero_inicial//10) % 10
            tercer_numero = numero_inicial - (primer_numero*100) - (segundo_numero*10) # tercer_numero = numero_inicial % 10
            suma = primer_numero + segundo_numero + tercer_numero
            break
        else:
            print("❌ Error: el número debe tener 3 dígitos.")
    except ValueError:
        print("❌ Error: debes introducir un número de 3 dígitos.")    
print(f"La suma de los 3 números que forman {numero_inicial} es: {primer_numero} + {segundo_numero} + {tercer_numero} = {suma}.")