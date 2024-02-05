def CalcularFactorial(num_munoz):
	if num_munoz == 1:
		return 1
	else:
		return num_munoz*CalcularFactorial(num_munoz-1)
