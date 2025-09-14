# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar de {numero}")
    for valor in range(1, 11):
        print(f"{numero} x {valor} = {numero * valor}")


numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

tabla_multiplicar(numero)

