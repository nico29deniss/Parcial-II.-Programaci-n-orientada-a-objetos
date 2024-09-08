# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla para título y autor (inmutable)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo_autor[0]} por {self.titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para los libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return f"El usuario {self.nombre} no tiene libros prestados."
        return f"Libros prestados por {self.nombre}:\n" + "\n".join([str(libro) for libro in self.libros_prestados])


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario: clave -> ISBN, valor -> Objeto Libro
        self.usuarios = {}  # Diccionario: clave -> ID usuario, valor -> Objeto Usuario
        self.usuarios_registrados = set()  # Conjunto para asegurar IDs únicos

    # Añadir un libro
    def anadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro {libro.titulo_autor[0]} añadido.")

    # Quitar un libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido removido.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    # Registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.usuarios_registrados.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado con éxito.")

    # Dar de baja un usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios[id_usuario]
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    # Prestar un libro a un usuario
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            usuario.prestar_libro(libro)
            del self.libros[isbn]  # Removemos el libro de la biblioteca
            print(f"Libro {libro.titulo_autor[0]} prestado a {usuario.nombre}.")
        else:
            print("Libro o usuario no encontrado.")

    # Devolver un libro a la biblioteca
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros[isbn] = libro  # Añadimos el libro de nuevo a la biblioteca
                    print(f"Libro {libro.titulo_autor[0]} devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    # Buscar un libro por título, autor o categoría
    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros.values() if getattr(libro, criterio) == valor]
        if resultados:
            print(f"Resultados de la búsqueda por {criterio} '{valor}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio} '{valor}'.")

    # Listar libros prestados
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.listar_libros_prestados()
        else:
            return "Usuario no encontrado."


def mostrar_menu():
    print("\nMenú de la Biblioteca:")
    print("1. Añadir/Quitar libros")
    print("2. Registrar/Dar de baja usuarios")
    print("3. Prestar/Devolver libros")
    print("4. Buscar libros")
    print("5. Listar libros prestados")
    print("6. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("1. Añadir libro")
            print("2. Quitar libro")
            subopcion = input("Seleccione una opción: ")
            if subopcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                categoria = input("Categoría: ")
                isbn = input("ISBN: ")
                libro = Libro(titulo, autor, categoria, isbn)
                biblioteca.anadir_libro(libro)
            elif subopcion == "2":
                isbn = input("ISBN del libro a quitar: ")
                biblioteca.quitar_libro(isbn)

        elif opcion == "2":
            print("1. Registrar usuario")
            print("2. Dar de baja usuario")
            subopcion = input("Seleccione una opción: ")
            if subopcion == "1":
                nombre = input("Nombre del usuario: ")
                id_usuario = input("ID del usuario: ")
                usuario = Usuario(nombre, id_usuario)
                biblioteca.registrar_usuario(usuario)
            elif subopcion == "2":
                id_usuario = input("ID del usuario a dar de baja: ")
                biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "3":
            print("1. Prestar libro")
            print("2. Devolver libro")
            subopcion = input("Seleccione una opción: ")
            if subopcion == "1":
                isbn = input("ISBN del libro a prestar: ")
                id_usuario = input("ID del usuario: ")
                biblioteca.prestar_libro(isbn, id_usuario)
            elif subopcion == "2":
                isbn = input("ISBN del libro a devolver: ")
                id_usuario = input("ID del usuario: ")
                biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "4":
            criterio = input("Buscar por (titulo, autor, categoria): ").strip()
            valor = input(f"Valor para buscar por {criterio}: ").strip()
            biblioteca.buscar_libro(criterio, valor)

        elif opcion == "5":
            id_usuario = input("ID del usuario para listar libros prestados: ")
            print(biblioteca.listar_libros_prestados(id_usuario))

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
