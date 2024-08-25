import os

# Clase Producto representa un producto individual en el inventario.
class Producto:
    def __init__(self, id, nombre, cantidad, precio, tienda):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
        self._tienda = tienda

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def get_tienda(self):
        return self._tienda

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def set_tienda(self, tienda):
        self._tienda = tienda

    # Método __str__ permite una representación legible del producto cuando se imprime.
    def __str__(self):
        return f'ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}, Tienda: {self._tienda}'

# Clase Inventario maneja una lista de productos y las operaciones sobre ellos.
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario_desde_archivo()

    def cargar_inventario_desde_archivo(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        id, nombre, cantidad, precio, tienda = linea.strip().split(',')
                        producto = Producto(id, nombre, int(cantidad), float(precio), tienda)
                        self.productos.append(producto)
                print(f"Inventario cargado desde {self.archivo}.")
            else:
                print(f"Archivo {self.archivo} no encontrado. Se creará un nuevo inventario.")
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo {self.archivo}.")
        except PermissionError:
            print(f"Error: No se tienen permisos para leer el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario_en_archivo(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f'{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()},{producto.get_tienda()}\n')
            print(f"Inventario guardado en {self.archivo}.")
        except PermissionError:
            print(f"Error: No se tienen permisos para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    # Añadir producto
    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print(f"Error: El producto con ID {producto.get_id()} ya existe.")
        else:
            self.productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' añadido con éxito.")
            self.guardar_inventario_en_archivo()

    # Eliminar producto
    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print(f"Producto con ID {id} eliminado con éxito.")
                self.guardar_inventario_en_archivo()
                return
        print(f"Error: Producto con ID {id} no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None, nueva_tienda=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                if nueva_tienda is not None:
                    producto.set_tienda(nueva_tienda)
                print(f"Producto con ID {id} actualizado con éxito.")
                self.guardar_inventario_en_archivo()
                return
        print(f"Error: Producto con ID {id} no encontrado.")

    # Buscar producto por nombre
    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    # Mostrar todos los productos
    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")

# Función de menú
def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad, precio o tienda de un producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            tienda = input("Ingrese el nombre de la tienda del producto: ")
            producto = Producto(id, nombre, cantidad, precio, tienda)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (o presione Enter para omitir): ")
            nuevo_precio = input("Ingrese el nuevo precio (o presione Enter para omitir): ")
            nueva_tienda = input("Ingrese el nuevo nombre de la tienda (o presione Enter para omitir): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_tienda = nueva_tienda if nueva_tienda else None

            inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio, nueva_tienda)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            print("Saliendo del sistema de gestión de inventario.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Verifica si el archivo se está ejecutando como script principal y llama al menú.
if __name__ == "__main__":
    menu()
