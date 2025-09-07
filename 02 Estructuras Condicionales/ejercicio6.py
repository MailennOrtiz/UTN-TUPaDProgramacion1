#6) Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"""
    Lista: {numeros_aleatorios}
    Moda: {moda}
    Mediana: {mediana}
    Media: {media}
    """)

if (media > mediana) and (mediana > moda):
    print("Sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo")
elif (media == mediana == moda):
    print("No hay sesgo")
else:
    print("No se cumple ninguna condición")