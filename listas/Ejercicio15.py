#Idoia Muñoz Otero
#Crear un programa de ordenador para gestionar los resultados_munoz de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:

#Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
#resultados: Es una tabla de enteros donde se indica el resultados_munoz También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
#de la tabla anterior, y en la segunda los goles del otro equipo.
#El programa ira pidiendo los nombres de los equipos de cada partido y el resultados_munozdel partido, a continuación se imprimirá la quiniela de esa jornada.

#¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?
equipos_munoz = []
resultados_munoz= []


num_jornadas = int(input("Ingrese el número de jornadas a registrar: "))
for jornada in range(1, num_jornadas + 1):
    print(f"\nJornada (jornada):")
    equipos_jornada = []
    resultados_munoz_jornada = []

    
    for partido in range(1, 16):
        equipo_local = input(f"Introduzca el nombre del equipo local del partido : ",(partido))
        equipo_visitante = input(f"Introduzca el nombre del equipo visitante del partido : ",(partido))
        equipos_jornada.append([equipo_local, equipo_visitante])

        goles_local = int(input(f"Introduzca los goles del equipo local {equipo_local}: "))
        goles_visitante = int(input(f"Introduzca los goles del equipo visitante {equipo_visitante}: "))
        resultados_munoz_jornada.append([goles_local, goles_visitante])

    equipos_munoz.append(equipos_jornada)
    resultados_munoz.append(resultados_munoz_jornada)


for jornada, (equipos_jornada, resultados_munoz_jornada) in enumerate(zip(equipos_munoz, resultados_munoz), start=1):
    print(f"\nJornada {jornada}:")
    for partido, ((equipo_local, equipo_visitante), (goles_local, goles_visitante)) in enumerate(zip(equipos_jornada, resultados_munoz_jornada), start=1):
        print(f"Partido {partido}: {equipo_local} {goles_local} - {goles_visitante} {equipo_visitante}")
