import json

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre            # Nombre del producto
        self.cantidad = cantidad        # Cantidad disponible del producto
        self.precio = precio            # Precio del producto

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __repr__(self):
        return f"Producto(ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio})"

# Clase que gestiona el inventario de productos
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos por ID

    # Añade un nuevo producto al inventario
    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    # Elimina un producto del inventario por su ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    # Actualiza los detalles de un producto existente
    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nombre is not None:
                producto.set_nombre(nombre)
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    # Busca productos por su nombre
    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.get_nombre() == nombre]
        return resultados

    # Muestra todos los productos en el inventario
    def mostrar_todos_productos(self):
        for producto in self.productos.values():
            print(producto)

    # Guarda el inventario en un archivo JSON
    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            json.dump(self.productos, archivo, default=lambda p: p.__dict__, indent=4)

    # Carga el inventario desde un archivo JSON
    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                datos = json.load(archivo)
                # Convierte los datos del archivo JSON en objetos Producto
                self.productos = {int(id_producto): Producto(**producto) for id_producto, producto in datos.items()}
        except FileNotFoundError:
            print("El archivo no existe.")

# Función principal que proporciona la interfaz de usuario
def menu():
    inventario = Inventario()
    archivo_inventario = 'inventario.json'
    inventario.cargar_desde_archivo(archivo_inventario)

    while True:
        print("\nMenú de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, nombre or None, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_producto_por_nombre(nombre)
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_todos_productos()

        elif opcion == '6':
            inventario.guardar_en_archivo(archivo_inventario)
            print("Inventario guardado. Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
