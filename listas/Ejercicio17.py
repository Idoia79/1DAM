#Idoia Muñoz Otero
#Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

listaoriginal_munoz = []
numero = int(input("Introduzca un número (negativo para terminar): "))

while numero >= 0:
    listaoriginal_munoz.append(numero)
    numero = int(input("Introduzca un número (negativo para terminar): "))


lista_sin_duplicados = list(set(listaoriginal_munoz))


print("Lista original:", listaoriginal_munoz)
print("Lista sin duplicados:", lista_sin_duplicados)