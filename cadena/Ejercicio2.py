#Idoia Munoz Otero
#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado
cadena_munoz= input("Introduce una cadena ")
subcadena_munoz= input("Introduce una subcadena ")
if  cadena_munoz.startswith(subcadena_munoz):
    print("Si comienza por la subcadena")
else:
    print("no comienza por la subcadena") 