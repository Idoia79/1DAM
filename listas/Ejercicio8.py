#Idoia Muñoz Otero
# Queremos guardar los nombres_munoz y la edades_munoz de los alumnos de un curso. 
# Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre 
# un asterisco (*) Al finalizar se mostrar� los siguientes datos:
#  * Todos lo alumnos mayores de edad.
#  * Los alumnos mayores (los que tienen más edad)

nombres_munoz = []
edades_munoz = []

while True:	
	nombre = input("Introduzca nombre de un alumno:")
	if nombre != "*":
		nombres_munoz.append(nombre)
		edades_munoz.append(int(input("Introduzca su edad:")))
	if nombre == "*": break;	


edad_max = max(edades_munoz)

print("Alumnos mayores de edad")
print("=======================")
for nombre,edad in zip(nombres_munoz,edades_munoz):
	if edad >= 18:
		print(nombre)
	


print("Alumnos mayores")
print("===============")
for nombre,edad in zip(nombres_munoz,edades_munoz):
	if edad == edad_max:
		print(nombre)
