#Idoia Muñoz Otero
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
#Ejemplo:
#Introduzca número del dado: 5
#En la cara opuesta está el "dos".
dado=int(input("Tira el dado que resultado es"))
#Declaramos las condicionales para que nos de la respuesta de la cara opuesta del dado
if dado==1:
    opuesta="seis"
elif dado==2:
    opuesta="cinco"
elif dado==5:
    opuesta="dos"   
elif dado==3:
    opuesta="cuatro"
elif dado==4:
    opuesta="tres"
else:
    opuesta="uno" 
print("la cara opuesta es",opuesta)



