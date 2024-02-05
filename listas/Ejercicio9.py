#Idoia Muñoz Otero
# Queremos guardar la temperatura mínima y máxima de 5 días. 
# Realiza un programa que de la siguiente información:

# * La temperatura media de cada día
# * Los días con menos temperatura
# * Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. 
# Si no existe ningún día se muestra un mensaje de información.

# Recorrido para rellenar la tabla (5 días con temp máxima y mínima)
temperatura_munoz = []
for indice in range(1,6):
	temperatura = []
	temperatura.append(int(input("Día  Temperatura máxima:" % indice)))
	temperatura.append(int(input("Día Temperatura mínima:" % indice)))
	temperatura_munoz.append(temperatura)

# Mostrar temperatura media
print("Temperaturas medias")
print("===================")

indice = 1
for temperatura in temperatura_munoz:
	print("Día . Temperatura media::" % (indice,sum(temperatura)/len(temperatura)))
	indice += 1


temp_min = temperatura_munoz[0][1];
for temperatura in temperatura_munoz:
	if temperatura[1] < temp_min:
		temp_min = temperatura[1]


print("Días con menos temperatura")
print("==========================")
indice = 1
for temperatura in temperatura_munoz:
	if temperatura[1] == temp_min:
		print("Día %d" % indice)
	indice +=1
	

existe_temperatura = False
print("Días con temperatura máxima")
print("===========================")
temp_max = int(input("Introduzca una temperatura:"))
indice = 1
for temperatura in temperatura_munoz:
	if temperatura[0] == temp_max:
		print("Día " % indice)
		existe_temperatura = True
	indice +=1
if not existe_temperatura:
	print("No hay ningún día con dicha temperatura.")
