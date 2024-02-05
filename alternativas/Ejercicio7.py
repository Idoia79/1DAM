#Idoia Muñoz Otero
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
# Calcular la potencia según el caso
base = float(input("Introduce la base de la potencia: "))
exponente = int(input("Introduce el exponente de la potencia: "))

if exponente > 0:
    # Si el exponente es positivo, usar la función pow o el operador **
    potencia = pow(base, exponente)
    # potencia = base ** exponente
elif exponente == 0:
    # Si el exponente es cero, el resultado es 1
    potencia = 1
else:
    # Si el exponente es negativo, el resultado es 1/potencia con el exponente positivo
    potencia = 1 / pow(base, -exponente)
    # potencia = 1 / (base ** -exponente)

# Mostrar el resultado
print(f"La potencia de {base} elevado a {exponente} es {potencia}")