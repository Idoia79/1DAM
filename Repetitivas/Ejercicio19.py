#Idoia Muñoz Otero
#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

while True:
    print("¿Que quieres de comer:")
    print("1. Ensalada")
    print("2. Macarrones")
    print("3. Carrillada")
    print("4. Flan")
    print("5. Salir")
    opcion_munoz = input(">> ")
    if opcion_munoz == "1":
        print("Has seleccionado  Ensalada.")
    elif opcion_munoz == "2":
        print("Has seleccionado  Macarrones.")
    elif opcion_munoz == "3":
        print("Has seleccionado  Carrillada.")
    elif opcion_munoz == "4":
        print("Has seleccionado la Flan.")
    elif opcion_munoz == "5":
        print("¡que aproveche!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")