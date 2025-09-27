# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra

frase = input("Ingrese una palabra o frase: ")

palabrasSeparadas = frase.split()

palabrasUnicas = set(palabrasSeparadas)

print(f"Palabras Únicas: {palabrasUnicas}")

contador = {}

for palabra in palabrasSeparadas:
    if palabra in contador:
        contador[palabra] += 1  # Si ya existe, sumamos 1
    else:
        contador[palabra] = 1   # Si no existe, la inicializamos en 1

print("Cantidad de cada palabra:", contador)