# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return round(segundos / 3600, 2)

segundos = int(input("Ingrese la cantidad de segundos para transformarlo en horas: "))

hora = segundos_a_horas(segundos)

print(f"{segundos} segundos son {hora} hora/s" )


