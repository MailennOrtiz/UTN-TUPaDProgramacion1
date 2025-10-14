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
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")

        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("---------------------------------------------")

agregarProducto = True

while agregarProducto: 
    print("Ingrese un nuevo producto:")
    nombre = input("Nombre:")
    precio = float(input("Precio:"))
    cantidad = int(input("Cantidad:"))

    with open ("productos.txt", "a") as archivo: 
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    opcionValida = True 

    while opcionValida == True:
        otroProducto = input("¿Desea agregar otro producto? (s/n): ").lower()
        if otroProducto == "n":
            agregarProducto = False
            opcionValida = False
        elif otroProducto == "s":
            agregarProducto = True
            opcionValida = False
        else:
            print("La opción ingresada no es válida, intente nuevamente.")
            opcionValida = True

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

productos = []

with open ("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()

        if linea: 
            nombre, precio, cantidad = linea.split(",")

            producto = {
                "nombre": nombre.strip(),
                "precio": float(precio.strip()),
                "cantidad": int(cantidad.strip())
            }

            productos.append(producto)

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error

buscarProducto = input("Para buscar un producto ingrese su nombre: ").lower()

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == buscarProducto:
        print(f"\nProducto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True
        break 

if not encontrado:
    print(f"\nEl producto '{buscarProducto}' no existe en la lista.")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
# productos actualizados desde la lista

with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")