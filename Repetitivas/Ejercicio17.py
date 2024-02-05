#Idoia Muñoz Otero
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N
sueldohora_munoz=int(input("¿Cuanto vale la hora?"))
empleados_munoz=int(input("¿Cuantos empleados tiene la empresa?"))
pagototal_munoz=0
horastotales_munoz=0
sueldosemanal_munoz=0
for i in range (empleados_munoz):
    dias_munoz=int(input("cuantos dias a la semana trabaja?"))
    
    for j in range (dias_munoz):
        horas_munoz=int(input("¿Cuantas horas trabaja al dia"))
       
        horastotales_munoz +=horas_munoz
        sueldodiario_munoz=(horastotales_munoz*sueldohora_munoz)
        sueldosemanal_munoz +=sueldodiario_munoz
        pagototal_munoz +=sueldosemanal_munoz
        
        print("cuanto es el sueldo semanal?",sueldosemanal_munoz)
        print("Cuanto paga la empresa ",pagototal_munoz)