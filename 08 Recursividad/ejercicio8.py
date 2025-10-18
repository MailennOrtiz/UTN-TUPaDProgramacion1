# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3 
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero == 0:
        return 0 
    else:
        ultimoNum = numero % 10
        return (1 if ultimoNum == digito else 0) + contar_digito(numero // 10, digito)

#------PROGRAMA PRINCIPAL-------

datosValidos = False 

while not datosValidos:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        digito = int(input("Ingrese un dígito (entre 0 y 9): "))
        
        if numero < 0:
            print("El número debe ser positivo. Intente nuevamente...")
        elif not (0 <= digito <= 9): 
            print("El dígito debe estar entre 0 y 9. Intente nuevamente...")
        else:
            resultado = contar_digito(numero, digito)
            print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
            datosValidos = True
            
    except ValueError:
        print("Ingrese solo números enteros positivos. Intente nuevamente...")