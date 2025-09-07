#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio donde se encuentra (Norte/Sur): ").lower()
mes = input("Ingrese el mes actual:").lower()
dia = int(input("Ingrese el día de hoy: "))

if (dia < 1) or (dia > 31):
    print("Ingrese un día válido (1 al 31)")
else:
    #HEMISFERIO NORTE --------------------------------------------------------
    if hemisferio == "norte": 
        if (mes == "enero") or (mes == "febrero"): #ENERO / FEBRERO - INVIERNO
            print("Estación actual: Invierno")
        elif (mes == "marzo"): #MARZO - INVIERNO / PRIMAVERA
            if (dia <= 20):
                print("Estación actual: Invierno")
            elif (dia > 20):
                print("Estación actual: Primavera")
        elif (mes == "abril") or (mes == "mayo"): #ABRIL / MAYO - PRIMAVERA
            print("Estación actual: Primavera")
        elif (mes == "junio"): #JUNIO - PRIMAVERA / VERANO
            if (dia <= 20):
                print("Estación actual: Primavera")
            elif (dia > 20):
                print("Estación actual: Verano")
        elif (mes == "julio") or (mes == "agosto"): #JULIO / AGOSTO - VERANO
            print("Estación actual: Verano")
        elif (mes == "septiembre"): #SEPTIEMBRE - VERANO / OTOÑO
            if (dia <= 20):
                print("Estación actual: Verano")
            elif (dia > 20):
                print("Estación actual: Otoño")
        elif (mes == "octubre") or (mes == "noviembre"): #OCTUBRE / NOVIEMBRE - OTOÑO
            print("Estación actual: Otoño")
        elif (mes == "diciembre"): #DICIEMBRE - OTOÑO / INVIERNO
            if (dia <= 20):
                print("Estación actual: Otoño")
            elif (dia > 20):
                print("Estación actual: Invierno")
        else:
            print("Ingrese un mes válido")
    elif hemisferio == "sur": #HEMISFERIO SUR ---------------------------------
        if (mes == "enero") or (mes == "febrero"): #ENERO / FEBRERO - VERANO
            print("Estación actual: Verano")
        elif (mes == "marzo"): #MARZO - VERANO / OTOÑO
            if (dia <= 20):
                print("Estación actual: Verano")
            elif (dia > 20):
                print("Estación actual: Otoño")
        elif (mes == "abril") or (mes == "mayo"): #ABRIL / MAYO - OTOÑO
            print("Estación actual: Otoño")
        elif (mes == "junio"): #JUNIO - OTOÑO / INVIERNO
            if (dia <= 20):
                print("Estación actual: Otoño")
            elif (dia > 20):
                print("Estación actual: Invierno")
        elif (mes == "julio") or (mes == "agosto"): #JULIO / AGOSTO - INVIERNO
            print("Estación actual: Invierno")
        elif (mes == "septiembre"): #SEPTIEMBRE - INVIERNO / PRIMAVERA
            if (dia <= 20):
                print("Estación actual: Invierno")
            elif (dia > 20):
                print("Estación actual: Primavera")
        elif (mes == "octubre") or (mes == "noviembre"): #OCTUBRE / NOVIEMBRE - PRIMAVERA
            print("Estación actual: Primavera")
        elif (mes == "diciembre"): #DICIEMBRE
            if (dia <= 20):
                print("Estación actual: Primavera")
            elif (dia > 20):
                print("Estación actual: Verano")
        else:
            print("Ingrese un mes válido")        
    else:    
        print("Ingrese un hemisferio válido")