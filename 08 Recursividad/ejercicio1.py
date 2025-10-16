# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario

def factorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

#------PROGRAMA PRINCIPAL-------

numeroValido = False

while not numeroValido:

    numeroFactorial = int(input("Ingrese un número entero positivo para calcular el factorial: "))
    
    if numeroFactorial >= 0:
        print(f"El factorial de {numeroFactorial} es: {factorial(numeroFactorial)}")

        if numeroFactorial == 0:
            pass
        else:
            print(f"Factorial de todos los números entre 1 y {numeroFactorial}")
        
            for i in range(1, numeroFactorial + 1):
                print(f"{i} = {factorial(i)}")

        numeroValido = True
    else: 
        print("El número ingresado no es válido. Intente nuevamente...")

