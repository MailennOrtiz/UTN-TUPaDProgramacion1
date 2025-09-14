# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

print("Para calcular el promedio entre números ingrese...")

numero1 = float(input("Numero 1:"))
numero2 = float(input("Numero 2:"))
numero3 = float(input("Numero 3:"))

promedio = calcular_promedio(numero1, numero2, numero3)

print(f"El promedio de los números: {numero1}, {numero2} y {numero3} es: {promedio}")