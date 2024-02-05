#Idoia Muñoz Otero
#Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila_munoz y todos los elementos de cada columna visualizando los resultados en pantalla
tablas_munoz = []
for indice_fila in range(1,6):
	fila_munoz = []
	for indice_col in range(1,6):
		fila_munoz.append(int(input("Introduzca el número de la fila_munoz %d y columna %d:" % (indice_fila,indice_col))))
	tablas_munoz.append(fila_munoz)


indice_fila = 1
for fila_munoz in tablas_munoz:
	print("La suma de los elemento de la fila_munoz %d es %d" % (indice_fila,sum(fila_munoz)))
	indice_fila += 1

# Suma las columnas
for indice_col in range(1,6):
	suma = 0
	for fila_munoz in tablas_munoz:
		suma = suma + fila_munoz[indice_col - 1]
	print("La suma de los elemento de la columna %d es %d" % (indice_col,suma))
