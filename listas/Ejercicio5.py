#Idoia Muñoz Otero
#Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.
import random
lista_munoz = []
for indice in range(1,11):
	lista_munoz.append(random.randint(1,10))
# Ordeno la lista_munoz
lista_munoz.sort()

# Recorro el vector ordenado
for numero in lista_munoz:
	print(numero," ",end="")
