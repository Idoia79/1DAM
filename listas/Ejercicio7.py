#Idoia Muñoz Otero
#Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
lista1_munoz=[]
lista2_munoz=[]
lista3_munoz=[]
for numeros in range(1,6):
    lista1_munoz.append(int(input("Introduzca numeros a la lista" %numeros)))
for numeros in range(1,6):
    lista2_munoz.append(int(input("Introduzca numeros a la lista" %numeros)))
for numeros in range(0,5):
    lista3_munoz.append(lista1_munoz[numeros]+lista2_munoz[numeros])
print("la suma de las listas es ")
for numero in lista3_munoz:
	print(numero," ",end="")
