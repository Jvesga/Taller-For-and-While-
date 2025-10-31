#Sistema de cálculo factorial que no solo computa el resultado final, 
#sino que muestra la descomposición paso a paso del proceso multiplicativo. 
#Incluye validación de dominio y análisis de crecimiento factorial.

numero= int(input("Ingrese un numero positivo para calcular su factorial: "))
resultado=numero
if numero < 0:
    print("Los factoriales no estan comprendidos para los numeros negativos, " \
    "debe ser positivo.")
else:
    for i in range(1, numero,1):
        resultado = resultado * i
        print(str(numero) + " x " + str(i) + " = " + str(resultado))
        print("")
    print("El factorial de " , numero , "es: " , resultado)