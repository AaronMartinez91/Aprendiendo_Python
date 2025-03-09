# Instrucción match (el equivalente en python de switch/case)

codigo = int(input("Introduce un código: "))

match codigo:
    case 200:
        print("El código 200, es todo correcto.")
    case 301: 
        print("El código 301, la página ha sido movida de lugar.")
    case 302: 
        print("El código 301, la página ha sido movida de forma temporal.") 
    case 404: 
        print("El código 404, la página no ha sido encontrada.")
    case _: # el case _: es la expeción de todas las otras, hace de comodín, es decir, no se corresponde con ninguno de los otros "case"
        print("Código no reconocido")