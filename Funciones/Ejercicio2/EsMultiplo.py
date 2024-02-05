def EsMultiplo(numero1_munoz, numero2_munoz):
    if numero2_munoz == 0:
        return False  # Evitar la división por cero
    return numero1_munoz % numero2_munoz == 0