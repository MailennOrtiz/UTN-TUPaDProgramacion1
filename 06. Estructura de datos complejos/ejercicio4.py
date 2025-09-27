# ) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {}

print("Ingrese 5 contactos nuevos")

for contador in range(5):
    nombre = input(f"Ingrese el nombre del contacto {contador + 1}:")
    numero = int(input(f"Ingrese el número de {nombre}: "))

    agenda[nombre] = numero

buscarNombre = input("Ingrese el nombre del contacto que quiere buscar:")

if buscarNombre in agenda:
    print(f"Su número es: {agenda[buscarNombre]}")