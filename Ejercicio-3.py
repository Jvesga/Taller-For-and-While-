# Programa que muestre la siguiente serie de números 
# basado en un número dado por el usuario
# 1
# 22
# 333
# 4444
# 55555
# 666666

print("---Serie de números----")
numero = int(input("Ingrese un numero positivo: "))

for i in range(1 , numero + 1):
    print(str(i) * i)      