#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

CORTE = 0 
numero = int(input(f"Ingrese un número entero para sumar ({CORTE} - Terminar Suma):"))

sumatoria = 0

while numero != CORTE:

    sumatoria += numero 
    numero = int(input(f"Ingrese otro número ({CORTE} - Terminar Suma)"))

print(f"La suma total de los números ingresados es: {sumatoria}")
