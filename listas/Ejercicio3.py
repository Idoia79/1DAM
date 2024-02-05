#Idoia Muñoz Otero
#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas_munoz, la nota media, la nota más alta que ha sacado y la menor.
notas_munoz = []
for indice in range(1,6):
	while True:
		nota = int(input("Introduzca la nota " % indice))
		if nota>=0 and nota<=10: break
	notas_munoz.append(nota)

# Muestro resultados

print("Notas: ",end="")
for nota in notas_munoz:
	print(nota," ",end="")
print()
print("Nota media: ",sum(notas_munoz)/len(notas_munoz))
print("Nota max: ",max(notas_munoz))
print("Nota min: ",min(notas_munoz))
