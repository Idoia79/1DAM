#Idoia Muñoz Otero
#Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:
#Zona	Ubicación	Costo/gramo
#1	América del Norte	24.00 euros
#2	América Central	20.00 euros
#3	América del Sur	21.00 euros
#4	Europa	10.00 euros
#5	Asia	18.00 euros
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
#Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega
zona=str(input("Introduzca la zona a la que va dirigida"))
cantidad=int(input("Introduzca cantidad de gramos"))
#Declaramos las condicionales para que nos diga cuanto cuesta la entrega y si nos hemos pasado de 5kg rechace la entrega
if cantidad>5000:
    print("Se rechaza la entrega")
else:
    if zona=="Amêrica del Norte":
     coste=cantidad*24
    elif zona=="América Central":
        coste=cantidad*20
    elif zona=="América del Sur":
       coste=cantidad*21
    elif zona=="Europa":
       coste=cantidad*10
    else:
       coste=cantidad*18
print("El precio de la entrega es",coste) 
    
    

