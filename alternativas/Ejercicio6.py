#Idoia Muñoz Otero
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
# Pedir una cadena por teclado
cadena = input("Introduce una cadena: ")

# Comprobar que la cadena al introducir una letra mayuscula te dice si lo es o no
if cadena.isupper():
        print("Has introducido una mayúscula")
else:
       print("No has introducido una mayúscula")