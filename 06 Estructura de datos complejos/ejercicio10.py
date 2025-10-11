# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia"
}

print("Diccionario original:", paises)

invertido = {}

for pais, capital in paises.items():
    invertido[capital] = pais

print("Diccionario invertido:", invertido)