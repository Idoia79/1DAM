#Idoia Muñoz Otero
#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo
import random
listanumeros_munoz=[]
for i in range(1,11):
    listanumeros_munoz.append(random.randint(1,10))
for numero in listanumeros_munoz:
    print(numero,"",numero**2,numero**3)