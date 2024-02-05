#Idoia Muñoz Otero
#Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:
#Se divide el número mayor entre el menor.
#Si la división es exacta, el divisor es el MCD.
#Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
#Crea un programa principal que lea dos números enteros y muestre el MCD.
from CalcularMCD import CalcularMCD
numero1_munoz = int(input("Número 1:"))
numero2_munoz = int(input("Número 2:"))
print("MCD: ", CalcularMCD(numero1_munoz,numero2_munoz))
