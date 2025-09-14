# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(numero1, numero2)

print(f"""Los resultados son...
    Suma = {resultados[0]}
    Resta = {resultados[1]}
    Multiplicación = {resultados[2]}
    División = {resultados[3]}
""")