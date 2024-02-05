#Idoia Muñoz otero
#Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
from CalcularMaxMin import CalcularMaxMin
import random
numeros = [] 

for i in range(10):
    numeros.append(random.randint(1,100))
vmax_munoz,vmin_munoz = CalcularMaxMin(numeros)
print("El valor máximo es ",vmax_munoz)
print("El valor mínimo es ",vmin_munoz)
