#Idoia Muñoz Otero
#Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla
lista1_munoz=[]
lista2_munoz=[]
for caracter in range(1,6):
    lista1_munoz.append(input("Dame la cadena %d:" % caracter))
lista2_munoz=lista1_munoz[::-1]
for cadena in lista2_munoz:
    print(cadena)