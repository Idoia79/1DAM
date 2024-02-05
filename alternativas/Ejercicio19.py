#Idoia Muñoz otero
#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente
Mes=int(input("Introduce el numero del mes"))
#Declaramos las condicionales de los meses que tienen 31,30 y 28 dias 
if Mes==1 or Mes==3 or Mes==5 or Mes==7 or Mes==8 or Mes==10 or Mes==12:
    print("el mes tiene 31 dias")
elif Mes==4 or Mes==6 or Mes==9:
    print("el mes tiene 30 dias")
elif Mes==2:
    print("el mes tiene 28 dias")
else:
    print("ha cometido un error")