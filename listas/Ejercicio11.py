#Idoia Muñoz Otero
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x5 y nombre 'diagonal'.
# Carga la tabla de forma que los componentes pertenecientes a la diagonal de la 
# tabla_munoz tomen el valor 1 y el resto el valor 0.
# Muestra el contenido de la tabla en pantalla.

tabla_munoz = []
for indice_fila in range(0,5):
	fila_munoz = []
	for indice_col in range(0,5): 
		
		if indice_fila == indice_col or indice_fila == 4 - indice_col:
			fila_munoz.append(1)
	
		else:
			fila_munoz.append(0)
	tabla_munoz.append(fila_munoz)

for fila_munoz in tabla_munoz:
	for elemento in fila_munoz:
		print(elemento," ",end="")
	print()
