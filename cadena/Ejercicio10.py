#Idoia Muñoz Otero
#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.
cadena_munoz=input("Introduce una cadena ")
cadenaresultante_munoz=cadena_munoz[::-1]
if cadenaresultante_munoz==cadena_munoz:
    print("la palabra es palíndroma ")
else:
    print("la palabra no espalíndroma")