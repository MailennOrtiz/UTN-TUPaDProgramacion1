#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numeroAleatorio = random.randint(0, 9)
numero = int(input("Adivina el número aleatorio. Ingrese el número que crea que es: "))

intentos = 1

while numeroAleatorio != numero:
    numero = int(input("Incorrecto! Intentalo nuevamente: "))

    intentos += 1

print(f"¡CORRECTO! - Intentos: {intentos}")
