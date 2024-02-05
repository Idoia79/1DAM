#Idoia Muñoz Otero
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio

while True:
    caracte_munoz = input("Introduce un caracte_munoz: ")
    
    if caracte_munoz == ' ':
        break
    
    if caracte_munoz.lower() == 'a' or caracte_munoz.lower() == 'e' or caracte_munoz.lower() == 'i' or caracte_munoz.lower() == 'o' or caracte_munoz.lower() == 'u':
        print("VOCAL")
    else:
        print("NO VOCAL")