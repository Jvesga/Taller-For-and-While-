#Módulo de seguridad que implementa verificación continua de credenciales 
#hasta obtener coincidencia exacta con el código de acceso autorizado. 
#Mantiene bucle de validación con retroalimentación al usuario.

print("----Inserte la credenciales del nuevo usuario----")
usuario = str(input("Ingrese su nombre de usuario: "))
contraseña = str(input("Ingrese su contraseña: "))

while True:
    print("Verificacion de credeciales")
    usuario1= str(input("Ingrese su nombre de usuario: "))
    contraseña1= str(input("Ingrese su contraseña: "))
    if usuario1 == usuario and contraseña1 == contraseña:
        print("Credenciales correctas")
        break
    else:
        print("Credenciales incorrectas")