#Idoia Muñoz Otero
#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario
x=int(input("Introduce el valor de x"))
y=int(input("Introduce el valor de y"))
#Declaramos la condicional en el caso de que sea cero el divisor no se pueda dividir, en los demas casos si
if y==0:
    print("no se puede dividir")
else:
    z=x/y
    print("el resultado es",z)
 