#Idoia Munoz Otero
#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.
cadena_munoz=input("Ingresa una cadena de texto: ")
caracter1_munoz=input("Ingresa el primer carácter: ")
caracter2_munoz=input("Ingresa el segundo carácter: ")

if len(caracter1_munoz) != 1 or len(caracter2_munoz) != 1:
    print("Los caracteres ingresados no son válidos.")
else:
    nueva_cadena=cadena_munoz.replace(caracter1_munoz, caracter2_munoz)
    print("La cadena modificada es:", nueva_cadena)