#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, 
#siempre que se conteste exactamente sí (en minúsculas y con tilde).

print("----La pregunta----")
print("--{Responda con si o no}--")

pregunta = input("¿Continuar?: ")

while pregunta == "si":
    print("--Continua--")
    pregunta = input("¿Continuamos?: ")
    
print("--Desidiste no continuar.--")