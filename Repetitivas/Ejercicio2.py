#Idoia Muñoz Otero
#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado
import random

secreto_munoz= random.randint(1, 100)
intentosmunoz = 10

print("¡Bienvenido al juego de adivinar el número!")
#Poner que pasa si es mayor que 0
while intentosmunoz > 0:
    print(f"Tienes {intentosmunoz} intentos restantes.")
    numero = int(input("Ingresa un número: "))
#poner que pasa si el numero es igual al numero secreto
    if numero == secreto_munoz:
        print(f"¡Felicidades! Adivinaste el número en {11 - intentosmunoz} intentos.")
        break
#poner que pasa si es mayor o menor
    elif numero < secreto_munoz:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")

    intentosmunoz -= 1

if intentosmunoz == 0:
    print(f"¡Te quedaste sin intentos! El número era {secreto_munoz}.")