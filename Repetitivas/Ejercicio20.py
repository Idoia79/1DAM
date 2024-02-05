#Idoia Muñoz Otero
#Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad_munoz de números primos que queremos mostrar

cantidad_munoz = int(input("Ingrese la cantidad de números primos que desea mostrar: "))
contador_munoz = 0
numero_munoz = 2

while contador_munoz < cantidad_munoz:
    es_primo = True
    for i in range(2, numero_munoz):
        if numero_munoz % i == 0:
            es_primo = False
            break
    if es_primo:
        print(numero_munoz)
        contador_munoz += 1
    numero_munoz += 1
    