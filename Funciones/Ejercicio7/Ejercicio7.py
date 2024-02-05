#Idoia Muñoz Otero
#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
from Login import Login
cuantasveces_munoz = 0
while True:
	usuario_munoz = input("Usuario:")
	clave_munoz = input("Password:")
	entrar,cuantasveces_munoz = Login(usuario_munoz,clave_munoz,cuantasveces_munoz)
	if not entrar:
		print("Error. Nombre de usuario o contraseña incorrecta.")
	if entrar or cuantasveces_munoz == 3: 
		break

if entrar:
	print("Bienvenidos al sistema")
else: 
	print("No has entrado en el sistema")
