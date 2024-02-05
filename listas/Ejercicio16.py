#Idoia Muñoz Otero
#Vamos a crear un programa que tenga el siguiente menú:

#Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
#Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
#Longitud de la lista: te muestra el número de elementos de la lista.
#Eliminar el último número: Muestra el último número de la lista y lo borra.
#Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
#Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
#Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
#Mostrar números: Muestra los números de la lista
#Salir
lista_munoz = []

while True:
    print("\n--- Menú ---")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero = int(input("Intruzca el número a añadir: "))
        lista_munoz.append(numero)
        print(f"Número {numero} añadido a la lista.")

    elif opcion == "2":
        numero = int(input("Introduzca el número a añadir: "))
        posicion = int(input("Introduzca la posición en la que añadir (1 en adelante): "))
        if 1 <= posicion <= len(lista_munoz) + 1:
            lista_munoz.insert(posicion - 1, numero)
            print(f"Número {numero} añadido en la posición {posicion}.")
        else:
            print("La posición no es válida.")

    elif opcion == "3":
        print(f"Longitud de la lista: {len(lista_munoz)}")

    elif opcion == "4":
        if lista:
            ultimo_numero = lista_munoz.pop()
            print(f"Último número de la lista: {ultimo_numero} ha sido eliminado.")
        else:
            print("La lista está vacía.")

    elif opcion == "5":
        posicion = int(input("Ingrese la posición del número a eliminar (1 en adelante): "))
        if 1 <= posicion <= len(lista_munoz):
            numero_eliminado = lista_munoz.pop(posicion - 1)
            print(f"Número {numero_eliminado} eliminado de la lista.")
        else:
            print("La posición no es válida.")

    elif opcion == "6":
        numero = int(input("Ingrese el número a contar: "))
        conteo = lista_munoz.count(numero)
        print(f"El número {numero} aparece {conteo} veces en la lista.")

    elif opcion == "7":
        numero = int(input("Introduzca el número para buscar sus posiciones: "))
        posiciones = [i + 1 for i, num in enumerate(lista_munoz) if num == numero]
        if posiciones:
            print(f"El número {numero} está en las posiciones: {', '.join(map(str, posiciones))}")
        else:
            print(f"El número {numero} no está en la lista.")

    elif opcion == "8":
        print("Números en la lista:", lista_munoz)

    elif opcion == "9":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 9.")
