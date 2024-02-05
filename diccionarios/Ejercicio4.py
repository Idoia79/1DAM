#Idoia Muñoz Otero
#Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas_munoz. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos_munoz y los valores serán listas con las notas_munoz de cada alumno.
#El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos_munoz y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.


num_alumnos = int(input("Introduzca el número de alumnos_munoz: "))
alumnos_munoz = {}

for _ in range(num_alumnos):
    nombre = input("Introduzca el nombre del alumno: ")
    
    # Verificar si el nombre del alumno ya existe en el diccionario
    while nombre in alumnos_munoz:
        print("¡Error! El nombre del alumno ya existe. Introduce un nombre diferente.")
        nombre = input("Introduzca el nombre del alumno: ")
    
    notas_munoz = []
    nota = float(input(f"Ingrese la nota del alumno {nombre} (introduzca un número negativo para terminar): "))
    
    while nota >= 0:
        notas_munoz.append(nota)
        nota = float(input(f"Ingrese la siguiente nota del alumno {nombre} (introduzca un número negativo para terminar): "))
    
    alumnos_munoz[nombre] = notas_munoz

# Mostrar la lista de alumnos_munoz y sus notas_munoz medias
print("\nLista de alumnos_munoz y sus notas_munoz medias:")
for nombre, notas_munoz in alumnos_munoz.items():
    if len(notas_munoz) > 0:
        media = sum(notas_munoz) / len(notas_munoz)
    else:
        media = 0
    print(f"{nombre}: Notas -> {notas_munoz}, Nota media -> {media:.2f}")
