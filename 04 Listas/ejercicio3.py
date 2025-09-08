#Crear una lista vacía, agregar tres palabras con append e imprimir la lista
#resultante por pantall. Pista: Para crear una lista vacía debes colocar los 
#corchetes sin nada en su interior.

lista = []

for contador in range(3):
    palabra = input("Ingrese una palabra:")
    lista.append(palabra)

print(lista)