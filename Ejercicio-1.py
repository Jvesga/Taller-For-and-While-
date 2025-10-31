#Programa que usando bucles permita pedir un numero par comprendido entre 100 y 200 y 
#muestre todos los numeros pares comprendidos entre el número ingresado y 200. 
#Por ejemplo, si el número ingresado es 192 nos debería mostrar 192, 194, 196, 198 y 200.

print("Ingrese un numero par entre 100 y 200: ")

numero = int(input("Ingrese un numero: "))

if numero < 100 or numero > 200 or numero %2 != 0:
    print("El numero ingresado no es correcto. Por favor inserte otro numero.")

 
print(f"Los numeros pares entre {numero} y 200 son: ")
for i in range(numero, 201, 2):
    print(i)