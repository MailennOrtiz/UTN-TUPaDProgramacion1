#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese el primer número:"))
numero2 = int(input("Ingrese el segundo número:"))
sumatoria = 0
contador = 0

numeroMayor = max(numero1, numero2) 
numeroMenor = min(numero1, numero2)

for contador in range(numeroMenor + 1, numeroMayor):
    sumatoria += contador 

print(f"La suma de los números comprendidos entre {numeroMenor} y {numeroMayor} es: {sumatoria}")
