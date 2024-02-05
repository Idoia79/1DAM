#Idoia Muñoz Otero
#Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.
dias_munoz = [31,28,31,30,31,30,31,31,30,31,30,31]
mes_munoz = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
while True:
	mes = int(input("Introduzca un mes (1-12):"))
	if mes < 1 or mes > 12:
		print("El mes no existe.")
	if mes>=1 and mes<=12: break
print("El mes de",mes_munoz[mes-1],"tiene",dias_munoz[mes-1],"días.")

