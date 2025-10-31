#Una planta que fabrica perfiles de hierro posee un lote de n piezas. 
#Desarrollar un programa que pida ingresar por teclado la cantidad de piezas a 
#procesar y luego ingrese la longitud de cada perfil; 
#sabiendo que la pieza cuya longitud esté comprendida en el rango de 1,20 y 1,30 son aptas. 
#Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

print("---Control de calidad---")
piezas=int(input("- Ingrese la cantidad de piezas a revisar: "))
piezas_aptas=0
contador=0

while True:
    L_Pieza=float(input("- Ingrese la longitud de la pieza: "))

    if L_Pieza <= 1.30 and L_Pieza >= 1.20:
        piezas_aptas = piezas_aptas + 1
        print("- La pieza es apta")

    else:
        L_Pieza < 1.20 or L_Pieza < 1.30
        print("- La pieza no es apta")
    
    contador = contador + 1

    if contador > (piezas - 1):
        break

print("- La cantidad de piezas aptas es de:", piezas_aptas)