#Idoia Muñoz Otero
#Escribir dos funciones que permitan calcular:
#La cantidad de segundoz en un tiempo dado en horas_munoz, minutos y segundos.
#La cantidad de horas, minutos y segundos_munoz de un tiempo dado en segundos.
#Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos_munoz o salir del programa.
from conversor_tiempo import tiempo_a_segundos_munoz, segundos_munoz_a_tiempo

from conversor_tiempo import tiempo_a_segundos_munoz, segundos_munoz_a_tiempo

def mostrar_menu():
    print("1. Convertir a segundos")
    print("2. Convertir a horas, minutos y segundos")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            horas_munoz = int(input("Ingrese las horas: "))
            minutos_munoz = int(input("Ingrese los minutos: "))
            segundos_munoz = int(input("Ingrese los segundos: "))
            resultado = tiempo_a_segundos_munoz(horas_munoz, minutos_munoz, segundos_munoz)
            print(f"El tiempo en segundos_munoz es: {resultado} segundos\n")

        elif opcion == "2":
            segundos_munoz = int(input("Ingrese la cantidad de segundos_munoz: "))
            horas_munoz, minutos_munoz, segundos_munoz = segundos_munoz_a_tiempo(segundos_munoz)
            print(f"El tiempo es: {horas_munoz} horas, {minutos_munoz} minutos, {segundos_munoz} segundos\n")

        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()