def CalcularMCD(num1_munoz,num2_munoz):
	from Intercambiar import Intercambiar
	num1_munoz, num2_munoz= Intercambiar(num1_munoz,num2_munoz)
	resto_munoz= num1_munoz % num2_munoz
	if resto_munoz== 0: 
		return num2_munoz
	else:
		return CalcularMCD(num2_munoz,resto_munoz)
