class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libros_por_autor(self, autor):
        libros_autor = []
        for libro in self.libros:
            if libro.autor.nombre == autor:
                libros_autor.append(libro)
        return libros_autor

    def prestar_libro(self, libro):
        if not libro.prestado:
            libro.prestado = True
            return True
        else:
            return False

    def devolver_libro(self, libro):
        libro.prestado = False

    def obtener_libros_prestados(self):
        libros_prestados = []
        for libro in self.libros:
            if libro.prestado:
                libros_prestados.append(libro)
        return libros_prestados


# Ejemplo de uso del sistema

# Crear autores
autor1 = Autor("Autor 1")
autor2 = Autor("Autor 2")

# Crear libros
libro1 = Libro("Libro 1", autor1)
libro2 = Libro("Libro 2", autor1)
libro3 = Libro("Libro 3", autor2)

# Crear biblioteca
biblioteca = Biblioteca()

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Buscar libros por autor
libros_autor1 = biblioteca.buscar_libros_por_autor("Autor 1")
print("Libros del Autor 1:")
for libro in libros_autor1:
    print(libro.titulo)

# Prestar un libro
if biblioteca.prestar_libro(libro1):
    print(f"El libro '{libro1.titulo}' ha sido prestado.")
else:
    print(f"El libro '{libro1.titulo}' no está disponible.")

# Mostrar libros prestados
libros_prestados = biblioteca.obtener_libros_prestados()
print("Libros prestados:")
for libro in libros_prestados:
    print(libro.titulo)

# Devolver un libro
biblioteca.devolver_libro(libro1)
print(f"El libro '{libro1.titulo}' ha sido devuelto.")
