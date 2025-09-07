# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo:"))
sumatoria = 0

if numero >= 0:
    for contador in range(numero + 1):
        sumatoria += contador
    print(f"La suma de todos los números comprendidos entre 0 y {numero} es: {sumatoria}")
else: 
    print("Número no válido! Debe ingresar un número positivo")

