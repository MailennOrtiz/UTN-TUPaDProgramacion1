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