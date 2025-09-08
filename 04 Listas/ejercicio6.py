# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros

numerosLista = []

for numero in range(10, 30 + 1, 5):
    numerosLista.append(numero)

print(f"""
    Primer número: {numerosLista[0]}
    Segundo número: {numerosLista[1]}
""")