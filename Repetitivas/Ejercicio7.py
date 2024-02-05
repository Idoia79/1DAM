#Idoia Muñoz Otero
#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado
numero_munoz=int(input("Introduce un numero"))
multiplicacion_munoz=0
for i in range(1,11):
    multiplicacion_munoz=numero_munoz*i
    print(numero_munoz,"x",i,"=",multiplicacion_munoz) 