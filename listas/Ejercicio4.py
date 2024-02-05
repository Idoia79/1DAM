#Idoia Muñoz Otero
#Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos)
lista_munoz = []
numero = int(input("Introduzca un número en la lista_munoz:"))
while numero>=0:
	lista_munoz.append(numero)
	numero = int(input("Introduzca un número en la lista_munoz:"))

for numero in lista_munoz:
	print(numero," ",end="")
