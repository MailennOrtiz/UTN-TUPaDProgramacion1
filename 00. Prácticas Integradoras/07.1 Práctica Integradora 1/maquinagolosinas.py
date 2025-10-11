#Se crea una lista con todos los productos
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

#Se crea el diccionario de empleados
empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

#Se crea la tupla de administración 
clavesTecnico = ("admin", "CCCDDD", "2020")

#Historial de golosinas pedidas
golosinasPedidas = []

opcion = 0
#--------------INICIO MÁQUINA DE GOLOSINAS -----------------

#Si el legajo es correcto puede acceder a la máquina

while opcion != 4: 
    #Se muestran las opciones y el usuario elige que acción hacer
    print("MÁQUINA DE GOLOSINAS")
    print("""
        Opciones:
        1. Pedir golosina
        2. Mostrar golosinas
        3. Rellenar golosinas
        4. Apagar maquina
        """)

    opcion = int(input("Ingrese la opción que desee (1-4): "))

    if opcion == 1: #-------------OPCIÓN 1---------------

        legajo = int(input("Ingrese su número de legajo: "))

        if legajo in empleados:
            #Muestra las opciones
            print ("""
                CÓDIGO / PRODUCTO 
                1. KitKat
                2. Chicles 
                3. Caramelos de Menta
                4. Huevo Kinder
                5. Chetoos
                6. Twix
                7. M&M'S
                8. Papas Lays
                9. Milkybar
                10. Alfajor Tofi
                11. Lata Coca
                12. Chitos
                """)
            verificacionCodigoGolosina = False

            while verificacionCodigoGolosina == False: 

                #El usuario ingresa el código de la golosina que desea 
                codigoGolosina = int(input("Ingrese el código de la golosina que desea retirar (1-12): "))

                #Si este se encuentra entre los valores 1 y 12 se van a realizar las siguientes acciones
                if codigoGolosina >= 1 and codigoGolosina <=12:
                    
                    golosinaElegida = golosinas[codigoGolosina-1][1]
                    restoGolosina = golosinas[codigoGolosina-1][2]

                    #Si hay golosinas en stock puede restar
                    if restoGolosina > 0:    
                        golosinas[codigoGolosina-1][2] -= 1 #Resta las golosinas extraídas y guarda las golosinas que quedan

                        print(f"Cantidad de golosinas actual: {golosinas[codigoGolosina-1][2]}")

                        encontrada = False
                        
                        for pedido in golosinasPedidas:
                            if pedido and pedido[0] == codigoGolosina:  # ya existe la golosina solo le suma uno al pedido
                                pedido[2] += 1
                                encontrada = True
                                break

                        if not encontrada:
                            # si no existe, se agrega una nueva fila: [código, nombre, cantidad]
                            golosinasPedidas.append([codigoGolosina, golosinaElegida, 1])

                        #Termina si se pudo realizar todo correctamente
                        verificacionCodigoGolosina = True

                        #Guarda el valor del nombre de la golosina
                    else:
                        #Si no hay mas golosinas podes elegir otra o salir
                        eleccion = input((f"Lo sentimos, la golosina {golosinaElegida} no se encuentra disponible, seleccione otra golosina o ingresa 'SALIR' si no desea otra golosina: "))

                        if eleccion.upper() == "SALIR":
                            verificacionCodigoGolosina = True
                else: 
                    print("El código no es válido, intente nuevamente")
        else:
            print("Usted no es un empleado de la empresa")
    elif opcion == 2:
        print("Cantidad de golosinas disponibles")
        for producto in golosinas:
            print(f"Código: {producto[0]} / Producto: {producto[1]} / Stock: {producto[2]}")

    elif opcion == 3:
        print("Sección Administrativa - Ingrese las 3 contraseñas correctamente para acceder")

        intentosCorrectos = 0

        for intento in range (1,4):
            contrasena = input(f"Ingrese la contraseña {intento}: ")

            if contrasena != clavesTecnico[intento-1]:
                print("Contraseña incorrecta.")
                intentosCorrectos = 0
                break

            intentosCorrectos +=1
                
        if intentosCorrectos == 3:
            print("Acceso Autorizado")
                
            codigoCorrecto = False
                    
            while codigoCorrecto == False:
                codigoRecargar = int(input("Ingrese el código del producto que quiere recargar (1-12): "))

                if 1 <= codigoRecargar <= 12:
                    codigoCorrecto = True
                else:
                    print("El dato ingresado no es válido.Intente nuevamente.")

            print(f"Stock Actual de {golosinas[codigoRecargar-1][1]}: {golosinas[codigoRecargar-1][2]}")

            cantidadValida = False

            while cantidadValida == False:
                cantidadRecargar = int(input("Ingrese la cantidad a recargar: "))

                if cantidadRecargar > 0:
                    cantidadValida = True
                
                    golosinas[codigoRecargar-1][2] += cantidadRecargar
                        
                    print(f"Stock actualizado. Cantidad actual: {golosinas[codigoRecargar-1][2]} unidades de {golosinas[codigoRecargar-1][1]}")

                    print("Recarga completada. Volviendo al menú principal.")
                else:
                    print("La cantidad debe ser mayor a 0.")
        else:
            print("No tiene permiso para ejecutar la función de recarga")
            continue

    elif opcion == 4:
        print("Apagando la máquina de golosinas...")
        print("Listado de golosinas pedidas durante la ejecución:")

        total_pedidas = 0
        for pedido in golosinasPedidas:
            print(f"Código: {pedido[0]} / Producto: {pedido[1]} / Cantidad pedida: {pedido[2]}")
            total_pedidas += pedido[2]  # se suma la cantidad de cada producto pedido

        print(f"Total de golosinas pedidas: {total_pedidas}")

#Si el número de legajo es incorrecto no va a dejar al usuario utilizar la máquina

print("Gracias por utilizar nuestros servicios!")
