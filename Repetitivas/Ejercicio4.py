#Idoia Muñoz Otero
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
contadorigual_munoz=0
contadormayor_munoz=0
contadormenor_munoz=0
numero_munoz=int(input("cuantos numeros quieres meter"))
for i in range (numero_munoz):
    valor_munoz=int(input("mete tu numero"))
    if valor_munoz==0:
            contadorigual_munoz +=1
    if valor_munoz>0:
            contadormayor_munoz +=1
    if valor_munoz<0:
            contadormenor_munoz +=1
print("hay tantos numeros iguales a o",contadorigual_munoz )
print("hay tantos numeros mayores a 0",contadormayor_munoz )
print("hay tantos numeros menores a 0",contadormenor_munoz)