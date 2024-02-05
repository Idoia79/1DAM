#Idoia Muñoz Otero
#Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.


preciofruta_munoz = {
    "manzana": 1.50,
    "platano": 0.75,
    "naranja": 0.90,
    "pera": 1.20
}

while True:
    fruta = input("Ingrese el nombre de la fruta: ")
    if fruta.lower() in preciofruta_munoz:
        cantidad = int(input("Ingrese la cantidad vendida: "))
        precio = preciofruta_munoz[fruta.lower()] * cantidad
        print("El precio final de", fruta, "es:", precio)
    else:
        print("¡Error! La fruta", fruta, "no existe en el diccionario.")

    respuesta = input("¿Desea hacer otra consulta? (s/n): ")
    if respuesta.lower() != "s":
        break