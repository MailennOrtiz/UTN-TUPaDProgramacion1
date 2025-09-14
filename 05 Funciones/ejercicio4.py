# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

import math

def calcular_area_circulo(radio):
    return round(math.pi * radio**2, 2) 

def calcular_perimetro_circulo(radio):
    return round(2 * math.pi * radio, 2) 


radio = float(input("Para calcular el área y el perímetro de un circulo ingresa el valor del radio: "))

resultadoArea = calcular_area_circulo(radio)
resultadoPerimetro = calcular_perimetro_circulo(radio)

print(F"El área es de: {resultadoArea} y el perímetro es: {resultadoPerimetro}")
