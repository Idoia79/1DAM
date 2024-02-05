#Idoia Muñoz Otero
#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena
cadena = input("Ingrese una cadena: ")
diccionario_munoz = {}
for caracter in cadena:
    diccionario_munoz[caracter] = diccionario_munoz.get(caracter, 0) + 1
print(diccionario_munoz)