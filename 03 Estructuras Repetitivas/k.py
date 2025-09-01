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
