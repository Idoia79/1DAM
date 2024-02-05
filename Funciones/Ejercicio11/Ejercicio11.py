#Idoia Muñoz Otero
#El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

#LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#EsBisiesto: Recibe un año y nos dice si es bisiesto.
#Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano


from utilidades_fecha import leer_fecha, calcular_dia_juliano

def main():
    print("Programa para calcular el día juliano de una fecha")
    fecha_munoz = leer_fecha()
    dia_juliano_munoz = calcular_dia_juliano(*fecha_munoz)
    print(f"El día juliano correspondiente a la fecha {fecha_munoz[0]}/{fecha_munoz[1]}/{fecha_munoz[2]} es: {dia_juliano_munoz}")

if __name__ == "__main__":
    main()