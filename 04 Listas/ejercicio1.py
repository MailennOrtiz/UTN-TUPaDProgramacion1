# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range

numeros = list(range(1,101))

for numero in numeros:
    if numero % 4 == 0:
        print(numero)