#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
#realizar un programa que lea los sueldos que cobra cada empleado e informe 
#cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
#Además, el programa deberá informar el importe que gasta la empresa en sueldos al personal.

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