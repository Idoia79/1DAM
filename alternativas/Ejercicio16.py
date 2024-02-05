#Idoia Muñoz Otero
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
duracion= int(input("Duración de la llamada en minutos: "))
dia = input("Día de la semana: ")
turno = input("Turno (mañana/tarde):")
#Declaramos las condicionales para calcular el precio de la llamada de teléfono
if duracion <= 5:
        costo = 1
elif duracion <= 8:
        costo = 1 + (duracion - 5) * 0.8
elif duracion <= 10:
        costo = 1 + 3 * 0.8 + (duracion - 8) * 0.7
else:
        costo = 1 + 3 * 0.8 + 2 * 0.7 + (duracion - 10) * 0.5
    
if dia == "domingo":
        costo *= 1.03
elif turno == "mañana":
        costo *= 1.15
elif turno == "tarde":
        costo *= 1.1
print("el costo de la llamada es",costo)

