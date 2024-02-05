#Idoia Muñoz Otero
#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

from EsMultiplo import EsMultiplo

def main():
    try:
        numero1_munoz = int(input("Ingrese el primer número entero: "))
        numero2_munoz = int(input("Ingrese el segundo número entero: "))
        
        if EsMultiplo(numero1_munoz, numero2_munoz):
            print(f"{numero1_munoz} es múltiplo de {numero2_munoz}.")
        elif EsMultiplo(numero2_munoz, numero1_munoz):
            print(f"{numero2_munoz} es múltiplo de {numero1_munoz}.")
        else:
            print("Ninguno de los números es múltiplo del otro.")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

if __name__ == "__main__":
    main()