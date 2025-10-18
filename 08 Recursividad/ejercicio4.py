# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

def decimalABinario(numero):
    if numero == 0:
        return ""
    else:
        return decimalABinario(numero // 2) + str(numero % 2)
        

#--------PROGRAMA PRINCIPAL---------

numeroValido = False

while not numeroValido: 

    numeroBaseDecimal = int(input("Ingrese un número entero positivo en base decimal: "))

    if numeroBaseDecimal >= 0:
        print(f"El número {numeroBaseDecimal} a binario es: {decimalABinario(numeroBaseDecimal)}")
        numeroValido = True  
    else:
        print("El número ingresado no es válido. Intente nuevamente...")