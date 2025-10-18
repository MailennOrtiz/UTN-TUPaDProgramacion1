# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)


def contar_bloques(numero):
    if numero == 0:
        return 0
    else:
        return numero + contar_bloques(numero - 1)

#-------PROGRAMA PRINCIPAL---------

esPositivo = False

while not esPositivo:
    try:
        numero = int(input("Ingrese el número de bloques en el nivel más bajo: "))
        
        if numero < 0:
            print("El número debe ser positivo. Intente nuevamente...")
        else:
            print(f"Se necesitan {contar_bloques(numero)} bloques para construir una pirámide")
            esPositivo = True
    except:
        print("El dato ingresado debe ser un número entero positivo. Intente nuevamente...")
        
