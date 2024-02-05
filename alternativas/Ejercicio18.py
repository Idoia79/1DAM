#Idoia Muñoz Otero
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.
semana= int(input("Introduzca el numero de la semana"))
#Declaramos las condicionales para que metiendo un numero del 1 al 7 nos diga el dia de la semana que esta en esa posición
if semana==1:
    print(" es lunes")
elif semana==2:
    print(" es martes")
elif semana==3:
    print(" es miercoles")
elif semana==4:
    print(" es jueves")
elif semana==5:
    print(" es viernes")
elif semana==6:
    print(" es sabado")
elif semana==7:
    print("es domingo")
else:
    print("ha cometido un error") 
