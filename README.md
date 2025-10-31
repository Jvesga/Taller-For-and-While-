# Taller-For-and-While

## Utilice ciclo for en los siguientes ejercicios
Programa que usando bucles permita pedir un número par comprendido entre 100 y 200 y muestre todos los números pares comprendidos entre el número ingresado y 200. Por ejemplo, si el número ingresado es 192 nos debería mostrar 192, 194, 196, 198 y 200.
```python
print("Ingrese un numero par entre 100 y 200: ")

numero = int(input("Ingrese un numero: "))

if numero < 100 or numero > 200 or numero %2 != 0:
    print("El numero ingresado no es correcto. Por favor inserte otro numero.")

 
print(f"Los numeros pares entre {numero} y 200 son: ")
for i in range(numero, 201, 2):
    print(i)
```
## 1.2.Simulador de cuenta regresiva que genera una secuencia descendente desde un valor inicial positivo hasta el punto de referencia cero. Utiliza iteración controlada para mostrar cada paso del conteo.
```python
numero=int(input("Ingrese un valor positivo para la cuenta regresiva: "))
if numero>0:
    for i in range(numero, -1, -1):
        print(i)
else:
    print("Por favor, ingrese un valor positivo.")
```
## 1.3.Programa que muestre la siguiente serie de números basado en un número dado por el usuario
<img width="380" height="261" alt="image" src="https://github.com/user-attachments/assets/d20078fe-8478-4e67-bc14-d367413e0721" />

```python
print("---Serie de números----")
numero = int(input("Ingrese un numero positivo: "))

for i in range(1 , numero + 1):
    print(str(i) * i)      
```
## 1.4.Sistema de cálculo factorial que no solo computa el resultado final, sino que muestra la descomposición paso a paso del proceso multiplicativo. Incluye validación de dominio y análisis de crecimiento factorial.
```python
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
```
## 2.Los siguientes ejercicios se deben realizar usando While o Do While
## 2.1.Módulo de seguridad que implementa verificación continua de credenciales hasta obtener coincidencia exacta con el código de acceso autorizado. Mantiene bucle de validación con retroalimentación al usuario.
```python
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
```
## 2.2.Sistema de cálculo salarial que procesa información laboral de múltiples empleados considerando horas trabajadas y tarifa horaria individual. Genera reporte consolidado de costos laborales.
```python
trabajador=int(input("Digite el numero de trabajadores: "))
salario_total_t=0
salarios_totales=0
trabajador1=1

while True:
    print(f"- trabajador numero {trabajador1}")
    horas=float(input("- Digite las horas trabajadas: "))
    valorhora=float(input("- Digite el valor por hora: "))
    salario_total_t=horas * valorhora
    print(f"- El salario del trabajador numero {trabajador1} es: {salario_total_t}")
    salarios_totales= salarios_totales + salario_total_t
    trabajador1= trabajador1 + 1
    if trabajador1 > trabajador:
        break
    print("")
print("El total de salios a pagar es de: " , salarios_totales)
```
## 2.1.Una planta que fabrica perfiles de hierro posee un lote de n piezas. Desarrollar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1,20 y 1,30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.
```python
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
```
## 2.2.En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además, el programa deberá informar el importe que gasta la empresa en sueldos al personal.
```python
n_empleados = int(input("Digite la cantidad de empreados: "))
total = 0
contador2_entre_100_200 = 0
contador3_mas_de_300 = 0
trabajador = 1

while trabajador <= n_empleados:
    paga = float(input(f"- Ingrese el salario del empleado {trabajador}: "))
    
    if paga >= 100 and paga <= 300:
        contador2_entre_100_200 = contador2_entre_100_200 + 1
    elif paga > 300:
        contador3_mas_de_300 = contador3_mas_de_300 + 1

    total = total + paga
    trabajador = trabajador + 1    

print("----Balance general de empleados y sueldos----")
print(f"Empleados que ganan entre 100 y 300 son: {contador2_entre_100_200}.")
print(f"Empleados que ganan mas de 300 son: {contador3_mas_de_300}.")
print(f"El pago total es de: {total}.")
```
## 2.3.Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).
```python
print("----La pregunta----")
print("--{Responda con si o no}--")

pregunta = input("¿Continuar?: ")

while pregunta == "si":
    print("--Continua--")
    pregunta = input("¿Continuamos?: ")
    
print("--Desidiste no continuar.--")
```
