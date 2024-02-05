#Idoia Muñoz Otero
#Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene
cadena_munoz=str(input("Introduce una cadena "))
palabras_munoz=cadena_munoz.split()
cantidadpalabras_munoz=len(palabras_munoz)
print("la cantidad de palabras es : ",cantidadpalabras_munoz)
