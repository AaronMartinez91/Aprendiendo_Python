
#! ALCANCE (SCOPE) de las variables globales y locales

cont_global = 0

def incrementar_contador():
    cont_local = 0       
    global cont_global      #? Con la palabra reservada "global" le indico que quiero acceder a la variable global para modificarla
    cont_global += 1
    cont_local += 1

    print(f"Contador local: {cont_local}")
    print(f"Contador global: {cont_global}")

#! Ivocamos a la función
incrementar_contador()
incrementar_contador()
incrementar_contador()  #? cada vez que invoco, accedo y aumento la global pero reinicio la local a 0, por eso solo varía la global
print(f"Valor de la variable global: {cont_global}")