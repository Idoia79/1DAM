#Idoia Muñoz Otero
#Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
# script_temperatura.py
from TemperaturaMedia import TemperaturaMedia

def main():
    try:
        num_dias = int(input("Ingrese el número de días: "))
        
        for i in range(num_dias):
            temp_max = float(input(f"Ingrese la temperatura máxima del día {i + 1}: "))
            temp_min = float(input(f"Ingrese la temperatura mínima del día {i + 1}: "))
            
            temp_media = TemperaturaMedia(temp_max, temp_min)
            
            print(f"La temperatura media del día {i + 1} es: {temp_media:.2f}°C")

    except ValueError:
        print("Por favor, ingrese números válidos.")

if __name__ == "__main__":
    main()
