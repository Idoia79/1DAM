def leer_fecha():
    dia_munoz = int(input("Ingrese el día: "))
    mes_munoz = int(input("Ingrese el mes: "))
    anio_munoz = int(input("Ingrese el año: "))
    return dia_munoz, mes_munoz, anio_munoz

def dias_del_mes(mes_munoz, anio_munoz):
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and es_bisiesto(anio_munoz):
        return 29

    return dias_por_mes[mes_munoz]

def es_bisiesto(anio_munoz):
    return (anio_munoz % 4 == 0 and anio_munoz % 100 != 0) or (anio_munoz % 400 == 0)

def calcular_dia_juliano(dia_munoz, mes_munoz, anio_munoz):
    dias_totales = dia_munoz

    for i in range(1, mes_munoz):
        dias_totales += dias_del_mes(i, anio_munoz)

    return dias_totales