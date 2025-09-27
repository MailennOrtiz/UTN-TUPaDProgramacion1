# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno

alumnosYNotas = {}

for contador in range(1,4):
    print("------------------------------------------------------")
    alumno = input(f"Ingrese el nombre del alumno {contador}: ")

    notasAlumnos = []

    print("\nIngrese las notas del alumno")
    for contadorNota in range(1,4):
        nota = int(input(f"Nota {contadorNota}: "))

        notasAlumnos.append(nota)
        
    notas = tuple(notasAlumnos)
    alumnosYNotas[alumno] = notas

print("\n--- Alumnos y notas ---")
print(alumnosYNotas)

print("\n--- Promedios ---")

for alumno, notas in alumnosYNotas.items():
    promedio = round(sum(notas) / len(notas), 2)
    print(f"{alumno}: {promedio}")


