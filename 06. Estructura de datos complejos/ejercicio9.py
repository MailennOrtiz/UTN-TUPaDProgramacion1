# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos

agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de Ingles",
    ("miércoles", "19:00"): "Clase de Yoga",
    ("jueves", "13:30"): "Cumpleaños Andrea"
}

dia = input("Ingrese un día para mostrar las actividades: ").lower()

encontrado = False

for clave, evento in agenda.items():
    if clave[0].lower() == dia:
        print(f"A las {clave[1]}: {evento}")
        encontrado = True

if not encontrado:
    print("No hay actividades en esa fecha.")
