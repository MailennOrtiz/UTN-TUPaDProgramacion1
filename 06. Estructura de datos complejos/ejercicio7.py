# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambosAprobados = parcial1 & parcial2
aprobaronUno = parcial1 ^ parcial2
estudiantesAprobados = parcial1 | parcial2

print(f"Alumnos que aprobaron ambos parciales: {ambosAprobados}")
print(f"Alumnos que aprobaron solo un parcial: {aprobaronUno}")
print(f"Alumnos que aprobaron al menos un parcial: {estudiantesAprobados}")
