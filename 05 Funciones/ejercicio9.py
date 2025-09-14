# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return round((celsius * 1.8) + 32, 2) 

celsius = float(input("Ingrese una temperatura en grados celsius para transformarla en grados Fahrenheit: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit}°F")