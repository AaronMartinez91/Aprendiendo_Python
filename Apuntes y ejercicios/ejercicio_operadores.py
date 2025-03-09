# Pedir usuario y contraseña y compararla con:
# usuario 'admin' y contraseña '1234'
usuario = "admin"
password = "1234"

comprobar_usuario = input("Por favor, introduzca su nombre de usuario: ").strip().lower()
comprobar_password = input("Por favor, introduzca su contraseña: ")

if comprobar_usuario == usuario and comprobar_password == password:
    print("El usuario y la contraseña son correctos.")
elif comprobar_usuario != usuario and comprobar_password == password:
    print("El usuario es incorrecto.")
elif comprobar_usuario == usuario and comprobar_password != password:
    print("La contraseña es incorrecta.")
else:
    print("El usuario y la contraseña son incorrectos.")