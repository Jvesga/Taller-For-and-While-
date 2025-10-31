#Sistema de cálculo salarial que procesa información laboral de múltiples 
#empleados considerando horas trabajadas y 
#tarifa horaria individual. 
#Genera reporte consolidado de costos laborales.

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
