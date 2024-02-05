#Idoia Muñoz Otero
#Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de
#lo que pagó después de los 20 meses.
pagos_munoz=10
totalpagar_munoz=0
for i in range(1,21):
        totalpagar_munoz +=pagos_munoz
print("El total a pagar es igual a ", totalpagar_munoz)
