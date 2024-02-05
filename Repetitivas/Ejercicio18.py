#Idoia Muñoz Otero
#Hacer un programa que muestre un cronometro, indicando las horas_munoz, minutos_munoz y segundos_munoz
import time

segundos_munoz = 0
minutos_munoz = 0
horas_munoz = 0

while True:
    print(f"{horas_munoz:02d}:{minutos_munoz:02d}:{segundos_munoz:02d}")
    time.sleep(1)
    segundos_munoz += 1

    if segundos_munoz == 60:
        segundos_munoz = 0
        minutos_munoz += 1

    if minutos_munoz == 60:
        minutos_munoz = 0
        horas_munoz += 1
while True:
    opcion = input("Presiona 's' para detener el cronómetro: ")
    
    if opcion.lower() == "s":
        detener_cronometro()
        break