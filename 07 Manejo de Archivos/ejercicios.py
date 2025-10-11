# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open ("productos.txt", "w") as archivo:
    archivo.write("Manzana,300,20\n")
    archivo.write("Naranja,250,35\n")
    archivo.write("Pera,200,10\n")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:

with open ("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    
    for linea in lineas:
        partes = linea.strip()
        nombre, precio, cantidad = linea.split(",")

        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("---------------------------------------------")

agregarProducto = True

while agregarProducto == True: 
    print("Ingrese un nuevo producto:")
    nombre = input("Nombre:")
    precio = float(input("Precio:"))
    cantidad = int(input("Cantidad:"))

    with open ("productos.txt", "a") as archivo: 
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    opcionValida = True 

    while opcionValida == True:
        otroProducto = input("¿Desea agregar otro producto? (s/n): ")
        if otroProducto.lower() == "n":
            agregarProducto = False
            opcionValida = False
        elif otroProducto.lower() == "s":
            agregarProducto = True
            opcionValida = False
        else:
            print("La opción ingresada no es válida, intente nuevamente.")
            opcionValida = True


