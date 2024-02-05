#Idoia Muñoz Otero
def EscribirCentrado(texto):
    longitud = len(texto)
    espacios_antes = 40 - longitud // 2
    mensaje_centralizado = ' ' * espacios_antes + texto
    subrayado = '=' * 80

    print(subrayado)
    print(mensaje_centralizado)
    print(subrayado)

if __name__ == "__main__":
    texto = input("Ingrese el texto que desea centrar: ")
    EscribirCentrado(texto)
