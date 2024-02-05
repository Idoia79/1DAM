#Idoia Muñoz Otero
#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
usuario = input("Introduce tu nombre de usuario: ")
contraseña = input("Introduce tu contraseña: ")

# Comprobar si el usuario y la contraseña son correctos
if usuario == "pepe" and contraseña == "asdasd":
    # Si son correctos, mostrar un mensaje de éxito
    print("Has entrado al sistema")
else:
    # Si no son correctos, mostrar un mensaje de error
    print("Usuario o contraseña incorrectos")