#DICCIONARIO ALUMNOS
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

#LISTA DE NOTAS FINALES - alumno / promedio 
notasFinales = [
    ["Rodolfo Fernandez"],
    ["Luis Gomez"],
    ["Andrea Pereira"], 
    ["Juan Cruz Gonzales"]]

#--------FUNCIONES----------#

def pedir_notas(): #Validar que la nota esté entre el 0 y el 10 
    while True:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        
        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
            promedio = (nota1 + nota2) / 2
            return nota1, nota2, round(promedio, 2)
        else:
            print("ERROR: El valor de ambas notas debe encontrarse entre 0 y 10. Intente nuevamente.")

#-------PROGRAMA PRINCIPAL--------

for alumno in alumnos: #Itera el diccionario de alumnos
    print(f"\nAlumno/a {alumnos[alumno]}")

    #LISTA DE MATERIAS - materia / nota 1 / nota 2 / promedio
    materias = [
        ["Ciencias"], 
        ["Historia"], 
        ["Geografía"], 
        ["Matemáticas"], 
        ["Fisica"]
    ]

    for materia in materias: #Itera la lista de materias y pide las notas
        print(f"Ingrese las notas para la materia {materia[0]} (0-10): ")

        nota1, nota2, promedio = pedir_notas()
    
        materia.append(nota1)
        materia.append(nota2)
        materia.append(promedio)

    print("\n--------------------------------------------")
    for fila in materias:
        print(f"{fila[0]} | Nota 1: {fila[1]} | Nota 2: {fila[2]} | Final: {fila[3]}")
    print("----------------------------------------------")

    calificacionMasAlta = 0

    for fila in materias: 
        if fila[3] >= calificacionMasAlta:
            calificacionMasAlta = fila[3]
            materiaCalificacionAlta = fila[0]
    print(f"La matería con la calificación más alta es {materiaCalificacionAlta} con un promedio de {calificacionMasAlta}")

    #Promedio general del alumno 

    sumaPromedios = 0

    for fila in materias:
        sumaPromedios += fila[3]
    
    promedioGeneral = round(sumaPromedios / 5, 2)

    for fila in notasFinales:
        if fila[0] == alumnos[alumno]:
            fila.append(promedioGeneral)
            break

    print(notasFinales)

promedioGeneralMayor = 0
alumnoPromedioMayor = ""

for fila in notasFinales:
    if len(fila) > 1:  
        if fila[1] > promedioGeneralMayor:
            promedioGeneralMayor = fila[1]
            alumnoPromedioMayor = fila[0]

print(f"El promedio más alto es {promedioGeneralMayor}, obtenido por el alumno/a {alumnoPromedioMayor}")


