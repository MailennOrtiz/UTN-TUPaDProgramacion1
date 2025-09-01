#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):
    print(numero)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
numero = abs(numero)
digitos = 0

if numero == 0:
    digitos = 1
else:
    digitos = 0
    while numero > 0:
        numero //= 10
        digitos += 1

print(f"El número contiene {digitos} digitos.")

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

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

CORTE = 0 
numero = int(input(f"Ingrese un número entero para sumar ({CORTE} - Terminar Suma):"))

sumatoria = 0

while numero != CORTE:

    if numero >= 0:
        sumatoria += numero 
    else:
        print("Número no válido, ingrese un número positivo")

    numero = int(input(f"Ingrese otro número ({CORTE} - Terminar Suma)"))

print(f"La suma total de los números ingresados es: {sumatoria}")