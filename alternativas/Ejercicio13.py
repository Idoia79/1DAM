#Idoia Muñoz Otero
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
#Declaramos las variables de que meses tienen 31, 30 o 28
meses_31_dias = [1, 3, 5, 7, 8, 10, 12]
meses_30_dias = [4, 6, 9, 11]
#Declaramos el condicionales para hacer el problema
if mes < 1 or mes > 12:
    print("el mes no existe")

    if dia < 1 or dia > 31:
        print("El dia no existe")

if mes == 2:
        if dia > 29:
            print("el mes 2 no tiene mas de 29 dias ")
        elif dia == 29 and not (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
             print("no tiene 29 dias")
if (dia, mes, anio):
    print("La fecha es correcta.")
else:
    print("La fecha es incorrecta.")   