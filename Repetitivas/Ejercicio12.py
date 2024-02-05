#Idoia Muñoz Otero
#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes
ahorroanual_munoz=0
for i in range(1,13):
    depositos_munoz=float(input("Indica cual es tu deposito"))
    ahorroanual_munoz +=depositos_munoz
    print("El ahorro anual es",ahorroanual_munoz)