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

    sumatoria += numero 
    numero = int(input(f"Ingrese otro número ({CORTE} - Terminar Suma)"))

print(f"La suma total de los números ingresados es: {sumatoria}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numeroAleatorio = random.randint(0, 9)
numero = int(input("Adivina el número aleatorio. Ingrese el número que crea que es: "))

intentos = 1

while numeroAleatorio != numero:
    numero = int(input("Incorrecto! Intentalo nuevamente: "))

    intentos += 1

print(f"¡CORRECTO! - Intentos: {intentos}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for contador in range(100, -1, -2):
    print(contador) 

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

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidadNumeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for contador in range(1, cantidadNumeros + 1):
    numero = int(input("Ingrese un número:"))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"""
    En los numeros ingresados hay...
    - {pares} pares
    - {impares} impares
    - {positivos} positivos
    - {negativos} negativos 
    """)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor)

cantidadNumeros = 5
sumatoria = 0

for contador in range(1, cantidadNumeros + 1):
    numero = int(input(f"Ingrese un número {contador}:"))

    sumatoria += numero

print(f"La media de los números ingresados es: {sumatoria / cantidadNumeros}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número:"))
numero_invertido = 0 

while numero != 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10

print(f"El número invertido es: {numero_invertido}")    