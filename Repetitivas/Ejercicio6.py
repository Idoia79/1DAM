#Idoia Muñoz Otero
#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario

numero1_munoz= int(input("introduce numero 1"))
numero2_munoz=int(input("Introduce numero2"))
for i in range(numero1_munoz,numero2_munoz+1):
    if i%2==0:
        print(i)