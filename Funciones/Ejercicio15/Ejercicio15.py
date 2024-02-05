#Idoia Muñoz Otero
#Vamos a realizar un programa similar al anterior para trabajar con unaco. Unaco es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el primer elemento_munoz que se añade al conjunto es el primero que se puede sacar.
#En realizada nos sirven todas las funciones del ejercicio anterior menos la función SacarDeLaCola que es la que tienes que modificar.
from utilidades_cola import (
    longitud_cola,
    esta_vacia_cola,
    esta_llena_cola,
    add_cola,
    sacar_de_la_cola,
    escribir_cola,
)

def mostrar_menu():
    print("1. Añadir elemento a la cola")
    print("2. Sacar elemento de la cola")
    print("3. Longitud de la cola")
    print("4. Mostrar cola")
    print("5. Salir")

def main():
    capacidad_cola = 5
    cola = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            elemento = input("Ingrese el elemento a añadir: ")
            add_cola(elemento, cola, capacidad_cola)

        elif opcion == "2":
            sacar_de_la_cola(cola)

        elif opcion == "3":
            print(f"Longitud de la cola: {longitud_cola(cola)}")

        elif opcion == "4":
            escribir_cola(cola)

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()