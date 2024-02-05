#Idoia Muñoz Otero
#Escribe un programa que dados dos números, uno real (base_munoz) y un entero positivo (exponente_munoz), saque por pantalla el resultado_munoz de la potencia. No se puede utilizar el operador de potencia.
base_munoz = float(input("Ingresa la base_munoz: "))
exponente_munoz = int(input("Ingresa el exponente_munoz: "))

resultado_munoz = 1
for _ in range(exponente_munoz):
    resultado_munoz *= base_munoz

print(f"El resultado_munoz de {base_munoz} elevado a la {exponente_munoz} es: {resultado_munoz}")


