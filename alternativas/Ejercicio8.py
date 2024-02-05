#Idoia Muñoz Otero
# Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el
#mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a
#dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe
#imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

nota = float(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ")
#Introducimos condicional de que si la nota es mayor que 5, la persona mayor que 18 y es de sexo femenino
if nota >= 5 and edad >= 18 and sexo == "F":
    print("ACEPTADA")
#Introducimos la condicional de lo mismo pero si es masculino
elif nota >= 5 and edad >= 18 and sexo == "M":
    print("POSIBLE")
#En el caso de que sea distinto a las anteriores 
else:
    print("NO ACEPTADA")