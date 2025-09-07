# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor)

cantidadNumeros = 5
sumatoria = 0

for contador in range(1, cantidadNumeros + 1):
    numero = int(input(f"Ingrese un número {contador}:"))

    sumatoria += numero

print(f"La media de los números ingresados es: {sumatoria / cantidadNumeros}")
