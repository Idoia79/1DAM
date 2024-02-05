#Idoia Muñoz Otero
#El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
#Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje

Alumnos=int(input("Introduce el numero de alumnos"))
#Introducimos la condicional para hayar el precio del viaje por alumno
if Alumnos>=100:
    costo=65
elif Alumnos>=50 and Alumnos<=99:
    costo=70
elif Alumnos>=30 and Alumnos<=49: 
    costo=95
else:
    costo=4000/Alumnos

print("el costo es", costo)
 
