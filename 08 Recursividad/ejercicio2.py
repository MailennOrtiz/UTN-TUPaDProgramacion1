# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique

def fibonacci(posicion):
    if posicion == 0:
        return 0 
    elif posicion == 1:
        return 1 
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

#----------PROGRAMA PRINCIPAL------------

numeroValido = False

while not numeroValido:
    posicionFibonacci = int(input("Ingrese un número entero para calcular el valor de la serie de Fibonacci: "))
    
    if posicionFibonacci >= 0:

        print("\n-------SERIE COMPLETA-------")
        for i in range(posicionFibonacci + 1):
            print(f"posición {i} = {fibonacci(i)}")

            numeroValido = True
    else:
        print("El número ingresado no es válido")
