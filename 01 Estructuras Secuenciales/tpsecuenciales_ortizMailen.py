#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio de un círculo para saber su área y perímetro: "))

area = 3.1416 * (radio)** 2
perimetro = 2 * 3.1416 * radio

print(f"Área: {area} / Perímetro: {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale

segundos = int(input("Ingrese una cantidad de segundos para calcular a cuántas horas equivale: "))

horas = segundos // 3600

print(f"{segundos} segundos, equivalen a {horas} hora/s.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un número para generar su tabla de multiplicación: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Para calcular la suma, resta, división y multiplicación entre dos números...")

numero1 = int(input("Ingrese el primer número (distinto a 0): "))
numero2 = int(input("Ingrese el segundo número (distinto a 0): "))

print("Resultados: ")
print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")
print(f"{numero1} / {numero2} = {numero1 / numero2}")
print(f"{numero1} * {numero2} = {numero1 * numero2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

print("Para calcular su índice de masa corporal...")

altura = float(input("Ingrese su altura (m): "))
peso = float(input("Ingrese su peso (kg): "))

indiceMasaCorporal = peso / (altura)** 2

print(f"El índice de masa corporal es de: {indiceMasaCorporal}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

print("Para calcular el equivalente de grados Celsius a Fahrenheit...")

temperatura_celsius = float(input("Ingrese una temperatura en grados Celsius: "))
temperatura_fahrenheit = ((9 / 5) * temperatura_celsius) + 32 

print(f"{temperatura_celsius}°C es equivalente a {temperatura_fahrenheit}°F")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

print("Para calcular un promedio...")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los números: {numero1}, {numero2} y {numero3} es {promedio}")