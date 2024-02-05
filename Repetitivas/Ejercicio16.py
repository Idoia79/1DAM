#Idoia Muñoz Otero
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados
sueldohora_munoz=int(input("¿Cuanto vale la hora?"))
empleados_munoz=int(input("¿Cuantos empleados tiene la empresa?"))
pagototal_munoz=0

for i in range (empleados_munoz):
    horas_munoz=int(input("¿cuantas horas semanales trabaja?"))
    sueldosemanal_munoz=sueldohora_munoz*horas_munoz
    pagototal_munoz +=sueldosemanal_munoz
    print("¿cuanto cobra semanalmente?",sueldosemanal_munoz)
print("¿cuanto pagara la empresa?",pagototal_munoz)
