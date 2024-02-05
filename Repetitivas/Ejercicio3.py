#Idoia Muñoz Otero
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos
suma_munoz=0
contador_munoz=0
while(True):
    numero_munoz= float(input("Introduce un número (introduce 0 para terminar): "))
    if numero_munoz==0:
        break
    suma_munoz +=numero_munoz
    contador_munoz+=1
    media_munoz=suma_munoz/contador_munoz
    print("La suma es",suma_munoz)
    print("la media es",media_munoz)
