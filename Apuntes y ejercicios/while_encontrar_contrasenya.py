# Dada una contraseña y un número máximo de intentos, decir si has encontrado o no la contraseña
# La contraseña es: "admin123"
# Límite de intentos máximo: 5 pruebas

password_secreto="admin123"
MAX_INTENTOS = 5
intentos = 0
acceso_concedido = False # no acabo de necesitar esta variable

while intentos < MAX_INTENTOS: # no es <= porque empezamos von la variable intentos = 0
    intento = input("Introduce la contraseña: ").strip()
    intentos += 1
    if intento == password_secreto:
        print("Acceso concedido.")
        break
    elif intentos < MAX_INTENTOS:
        print(f"Contraseña incorrecta, te quedan {MAX_INTENTOS-intentos} intentos restantes.")
    else:
        print("Has gastado todos tus intentos, tu cuenta se bloqueará.")

