#Idoia Muñoz Otero
#Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

import math

numero_munoz = int(input("Introduce un número: "))

if numero_munoz < 2:
    primo_munoz = False
else:
    primo_munoz = True
    for i in range(2, int(math.sqrt(numero_munoz)) + 1):
        if numero_munoz % i == 0:
            primo_munoz = False
            break

if primo_munoz:
    print(numero_munoz, "es un número primo.")
else:
    print(numero_munoz," no es un número primo.")