#Idoia Muñoz Otero
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
#se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

tipo_uva = input("Ingrese el tipo de uva (A o B): ")
tamaño_uva = int(input("Ingrese el tamaño de la uva (1 o 2): "))
precio_inicial_uva = float(input("Ingrese el precio inicial por kilo de uva: "))
#Declaramos las condicionales para calcular la ganancia de las uvas
if tipo_uva=="A" and tamaño_uva==1:
    ganancia=precio_inicial_uva+0.20
elif tipo_uva=="A" and tamaño_uva==2:
    ganancia=precio_inicial_uva+0.30

elif tipo_uva=="B" and tamaño_uva==1:
        ganancia=precio_inicial_uva-0.30
elif tipo_uva=="B" and tamaño_uva==2:
    ganancia=precio_inicial_uva-0.50
else:
     print("ha cometido un error")
print("la ganancia por kilo es", ganancia)