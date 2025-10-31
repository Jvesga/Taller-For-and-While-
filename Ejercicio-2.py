#Simulador de cuenta regresiva que genera una secuencia descendente desde un valor 
#inicial positivo hasta el punto de referencia cero. 
#Utiliza iteración controlada para mostrar cada paso del conteo.

numero=int(input("Ingrese un valor positivo para la cuenta regresiva: "))
if numero>0:
    for i in range(numero, -1, -1):
        print(i)
else:
    print("Por favor, ingrese un valor positivo.")