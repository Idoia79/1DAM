def leer_fraccion():
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    return simplificar_fraccion(numerador, denominador)

def escribir_fraccion(numerador, denominador):
    if denominador == 1:
        print(f"{numerador}")
    else:
        print(f"{numerador}/{denominador}")

def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def simplificar_fraccion(numerador, denominador):
    mcd = calcular_mcd(numerador, denominador)
    return numerador // mcd, denominador // mcd

def sumar_fracciones(n1, d1, n2, d2):
    numerador = n1 * d2 + d1 * n2
    denominador = d1 * d2
    return simplificar_fraccion(numerador, denominador)

def restar_fracciones(n1, d1, n2, d2):
    numerador = n1 * d2 - d1 * n2
    denominador = d1 * d2
    return simplificar_fraccion(numerador, denominador)

def multiplicar_fracciones(n1, d1, n2, d2):
    numerador = n1 * n2
    denominador = d1 * d2
    return simplificar_fraccion(numerador, denominador)

def dividir_fracciones(n1, d1, n2, d2):
    numerador = n1 * d2
    denominador = d1 * n2
    return simplificar_fraccion(numerador, denominador)