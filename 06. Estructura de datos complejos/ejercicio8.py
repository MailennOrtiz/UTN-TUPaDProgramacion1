# Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe

print("---------- Productos ----------\n")
productos = {
    "chicles": 30, 
    "maní Saborizado": 15,
    "papas": 10,
    "oreos": 5,
    "chocolate": 3 }

print(f"{sorted(productos)}\n")
print("--------------------------------")

nombre = input("Ingrese el nombre del producto: ").lower()

# Se verifica si está en el diccionario
if nombre in productos:
    print(f"Stock actual de {nombre}: {productos[nombre]} unidades")
    
    # Agregar stock si es necesario
    agregar = input("¿Querés agregar unidades al stock? (s/n): ").lower()
    if agregar == "s":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        productos[nombre] += unidades
        print(f"Stock actualizado de {nombre}: {productos[nombre]} unidades")
else:
    print(f"El producto '{nombre}' no existe")
    agregar_nuevo = input("¿Querés agregarlo como un nuevo producto? (s/n): ").lower()
    if agregar_nuevo == "s":
        unidades = int(input("¿Cuántas unidades tiene?: "))
        productos[nombre] = unidades
        print(f"Producto '{nombre}' se ha agregado con {unidades} unidades de stock")

# Se muestra el estado final del diccionario
print("\nStock actual de todos los productos:")
for producto, stock in productos.items():
    print(f"{producto}: {stock} unidades")