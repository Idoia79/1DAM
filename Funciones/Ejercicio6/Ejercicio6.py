#Idoia Muñoz Otero
#Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
from CalcularAreaPerimetro import CalcularAreaPerimetro
radio_munoz = float(input("Introduce el radio:"))
area_munoz,perimetro_munoz = CalcularAreaPerimetro(radio_munoz)
print("Área:",area_munoz)
print("Perímetro:",perimetro_munoz)
