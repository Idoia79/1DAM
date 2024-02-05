#Idoia Muñoz Otero
#De una empresa de transporte se quiere guardar el nombre_munoz de los conductores que tiene, y los kilómetros que conducen cada día de la semana.

#Para guardar esta información se van a utilizar dos arreglos:

#Nombre: Lista para guardar los nombres de los conductores.
#kms_munoz: Tabla para guardar los kilómetros que realizan cada día de la semana.
#Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.

#Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.
dias_munoz =["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
nombre_munoz = []
kms_munoz = []

while True:
	num_conductores = int(input("¿Cuántos conductores tiene la empresa?:"))
	if num_conductores>0: break


for indice_cond in range(0,num_conductores):
	nombre_munoz.append(input("Nombre del conductor %d:" % (indice_cond + 1)))
	
	kmdias_munoz = []
	for indice_dias in range(0,7):
		kmdias_munoz.append(int(input("¿Cuántos km ha realizado el %s?:" % dias_munoz[indice_dias])))
	kms_munoz.append(kmdias_munoz)

totalkm_munoz = []
for km in kms_munoz:
	totalkm_munoz.append(sum(km))

for nombre_munoz, km in zip(nombre_munoz, totalkm_munoz):
	print("%s  ha realizado %d kms_munoz." % (nombre_munoz,km))
