class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no está disponible."

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"El libro '{self.titulo}' ya estaba en la biblioteca."

    def informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\nEstado: {estado}"


def main():
    libro1 = Libro("El señor de los anillos", "tolkien", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

    print("Información inicial de los libros")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())
    print("\n")

    print("Prestamo de librs")
    print(libro1.prestar())
    print(libro2.prestar())
    print("\n")

    print("Intento de prestamo de libros ya prestados")
    print(libro1.prestar())
    print("\n")

    print("Informacion despues del prestamo")
    print(libro1.informacion())
    print("\n")

    print("Devolucion de libros")
    print(libro1.devolver())
    print("\n")

    print("Intento de devolucion de libros ya disponibles")
    print(libro1.devolver())
    print("\n")

    print("Informacion final de los libros")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())


if __name__ == "__main__":
    main()
