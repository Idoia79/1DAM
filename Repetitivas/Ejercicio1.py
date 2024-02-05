#Idoia Muñoz Otero
#Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120),
numero_munoz = int(input("Ingresa un número: "))
factorial_munoz = 1

if numero_munoz < 0:
    print("El factorial no está definido para números negativos.")
elif numero_munoz == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, numero_munoz + 1):
        factorial_munoz *= i
    print("El factorial de", numero_munoz, "es:", factorial_munoz)
    