#Idoia Muñoz Otero
#Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar.
#Para representar una pila vamos a utilizar una lista de cadenas de caracteres.

#Vamos a crear varias funciones para trabajar con la pila:

#LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.
#EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.
#EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.
#AddPila: función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, si no está llena. si esta llena muestra un mensaje de error.
#SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía muestra un mensaje de error.
#EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.
#Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, con las siguientes opciones:

#Añadir elemento a la pila
#Sacar elemento de la pila
#Longitud de la pila
#Mostrar pila
#Salir



from utilidades_pila import (
    longitud_pila,
    esta_vacia_pila,
    esta_llena_pila,
    add_pila,
    sacar_de_la_pila,
    escribir_pila,
)

def mostrar_menu():
    print("1. Añadir elemento a la pila")
    print("2. Sacar elemento de la pila")
    print("3. Longitud de la pila")
    print("4. Mostrar pila")
    print("5. Salir")

def main():
    capacidad_pila_munoz = 5
    pila = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            elemento = input("Ingrese el elemento a añadir: ")
            add_pila(elemento, pila, capacidad_pila_munoz)

        elif opcion == "2":
            sacar_de_la_pila(pila)

        elif opcion == "3":
            print(f"Longitud de la pila: {longitud_pila(pila)}")

        elif opcion == "4":
            escribir_pila(pila)

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()