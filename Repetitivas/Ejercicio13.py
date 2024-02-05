#Idoia Muñoz Otero
#Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas
sueldohora_munoz=int(input("¿Cuanto vale la hora?"))
horas_munoz=0
for i in range(1,7):
    horasdia_munoz=int(input("¿cuantas horas trabaja al dia?"))
    horas_munoz +=horasdia_munoz
    print("El numero de horas asciende a ",horas_munoz)

sueldo_munoz=sueldohora_munoz*horas_munoz
print("El sueldo asciende a ", sueldo_munoz)