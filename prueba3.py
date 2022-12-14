#creacion de usuario y contraseña
usuario = "admin"
contraseña = "12345"

#validacion de datos
while True:
    try:
        usuario_ingresado = input("Ingrese su usuario: ")
        contraseña_ingresada = input("Ingrese su contraseña: ")
        if usuario_ingresado == usuario and contraseña_ingresada == contraseña:
            print("Bienvenido al sistema")
            break
        else:
            print("Usuario o contraseña incorrectos")
    except:
        print("Error al ingresar los datos")