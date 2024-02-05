def tiempo_a_segundos(horas_munoz, minutos_munoz, segundos_munoz):
    return horas_munoz * 3600 + minutos_munoz * 60 + segundos_munoz

def segundos_a_tiempo(segundos_munoz):
    horas_munoz = segundos_munoz // 3600
    segundos_munoz %= 3600
    minutos_munoz = segundos_munoz // 60
    segundos_munoz %= 60
    return horas_munoz, minutos_munoz, segundos_munoz

