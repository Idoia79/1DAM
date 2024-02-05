#Idoia Muñoz Otero
#Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

#Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
#Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
#Eliminar: Me pide una cadena, y la elimina de la lista.
#Mostrar: Muestra la lista de cadenas
#Terminar
listapalabras_munoz = []

while True:
    print("\n--- Menú ---")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Terminar")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        palabra_contar = input("Introduzca la palabra a contar: ")
        conteo = listapalabras_munoz.count(palabra_contar)
        print(f"La palabra '{palabra_contar}' aparece {conteo} veces en la lista.")

    elif opcion == "2":
        palabra_modificar = input("Introduzca la palabra a modificar: ")
        nueva_palabra = input("Ingrese la nueva palabra: ")
        listapalabras_munoz = [nueva_palabra if palabra == palabra_modificar else palabra for palabra in listapalabras_munoz]
        print(f"Se modificaron las apariciones de '{palabra_modificar}' por '{nueva_palabra}'.")

    elif opcion == "3":
        palabra_eliminar = input("Introduzca la palabra a eliminar: ")
        listapalabras_munoz = [palabra for palabra in listapalabras_munoz if palabra != palabra_eliminar]
        print(f"Se eliminaron todas las apariciones de '{palabra_eliminar}'.")

    elif opcion == "4":
        print("Lista de palabras:", listapalabras_munoz)

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")