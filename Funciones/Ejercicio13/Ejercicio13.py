#Idoia Muñoz Otero
#Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.

#Vamos a crear las siguientes funciones para trabajar con funciones:

#Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
#Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
#Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
#Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
#Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado_munoz.
#Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado_munoz.
#Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado_munoz.
#Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado_munoz.
#Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:

#Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado_munoz.
#Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
#Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
#Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
#Salir



from utilidades_fracciones import (
    leer_fraccion,
    escribir_fraccion,
    sumar_fracciones,
    restar_fracciones,
    multiplicar_fracciones,
    dividir_fracciones,
)

def mostrar_menu():
    print("1. Sumar dos fracciones")
    print("2. Restar dos fracciones")
    print("3. Multiplicar dos fracciones")
    print("4. Dividir dos fracciones")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            fraccion1_munoz = leer_fraccion()
            fraccion2_munoz = leer_fraccion()
            resultado_munoz = sumar_fracciones(*fraccion1_munoz, *fraccion2_munoz)
            print("El resultado_munoz de la suma es:")
            escribir_fraccion(*resultado_munoz)

        elif opcion == "2":
            fraccion1_munoz = leer_fraccion()
            fraccion2_munoz = leer_fraccion()
            resultado_munoz = restar_fracciones(*fraccion1_munoz, *fraccion2_munoz)
            print("El resultado_munoz de la resta es:")
            escribir_fraccion(*resultado_munoz)

        elif opcion == "3":
            fraccion1_munoz = leer_fraccion()
            fraccion2_munoz = leer_fraccion()
            resultado_munoz = multiplicar_fracciones(*fraccion1_munoz, *fraccion2_munoz)
            print("El resultado_munoz de la multiplicación es:")
            escribir_fraccion(*resultado_munoz)

        elif opcion == "4":
            fraccion1_munoz = leer_fraccion()
            fraccion2_munoz = leer_fraccion()
            resultado_munoz = dividir_fracciones(*fraccion1_munoz, *fraccion2_munoz)
            print("El resultado_munoz de la división es:")
            escribir_fraccion(*resultado_munoz)

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()