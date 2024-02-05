#Idoia Muñoz Otero
#Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
ano=int(input("Introduce un año"))
#Introducimos las condicionales para determinar si un año es bisiesto
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("El año es bisiesto")
else:
    print("el año no es bisiesto") 