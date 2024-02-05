#Idoia Muñoz Otero
#Diseñar el algoritmo correspondiente a un programa, que:

#Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
#Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.

#111111111111111
#100000000000001
#100000000000001
#100000000000001
#111111111111111
#Visualiza el contenido de la matriz en pantalla.
marco_munoz = []
num_filas = 5
num_cols = 15
for indice_fila in range(0,num_filas):
	fila_munoz = []
	for indice_col in range(0,num_cols): 
		
		if indice_fila == 0 or indice_fila == num_filas - 1 or indice_col == 0 or indice_col == num_cols -1:
			fila_munoz.append(1)
		else:
			fila_munoz.append(0)
	marco_munoz.append(fila_munoz)

for fila_munoz in marco_munoz:
	for elemento in fila_munoz:
		print(elemento," ",end="")
	print()
