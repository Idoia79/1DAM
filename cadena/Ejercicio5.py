#Idoia Muñoz Otero
#Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales_munoz en mayúsculas
nombreapellidos_munoz = input("Escribe tu nombre y apellidos: ")
palabras_munoz = nombreapellidos_munoz.split()
iniciales_munoz = ""
for palabra in palabras_munoz:
  
    inicial_munoz = palabra[0].upper()
    iniciales_munoz += inicial_munoz

# Mostramos las iniciales_munoz en mayúsculas
print("\nNombres y Apellidos con primera letra en Mayúscula:",iniciales_munoz)

