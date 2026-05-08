class Prestamo:
    """Representa un registro de prestamo de un equipo."""

    def __init__(self, usuario: str, fecha: str):
        self.usuario = usuario
        self.fecha = fecha

    def __str__(self):
        return f"Usuario: {self.usuario}, Fecha: {self.fecha}"


class Equipo:
    """Representa un equipo dentro del inventario."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.disponible = True
        self.prestamos: list[Prestamo] = []

    def esta_disponible(self) -> bool:
        return self.disponible

    def prestar(self, usuario: str, fecha: str):
        prestamo = Prestamo(usuario, fecha)
        self.prestamos.append(prestamo)
        self.disponible = False

    def devolver(self):
        self.disponible = True

    def obtener_estado(self) -> str:
        return "Disponible" if self.disponible else "Prestado"

    def __str__(self):
        return f"{self.nombre} - {self.obtener_estado()}"


class SistemaPrestamos:
    """Gestiona el inventario de equipos y las operaciones del sistema."""

    def __init__(self):
        self.inventario: dict[str, Equipo] = {}
        self._cargar_equipos_iniciales()

    def _cargar_equipos_iniciales(self):
        nombres_iniciales = [
            "Laptop HP",
            "Monitor Dell",
            "Teclado Logitech",
            "Mouse inalambrico",
        ]
        for nombre in nombres_iniciales:
            self.inventario[nombre] = Equipo(nombre)

    # ----------------------------------------------------------
    #  Operaciones del sistema
    # ----------------------------------------------------------

    def mostrar_equipos(self):
        print("\nEquipos en el sistema")
        for equipo in self.inventario.values():
            print(equipo)

    def registrar_prestamo(self):
        print("\nRegistrar Prestamo")
        self.mostrar_equipos()

        nombre = input("\nIngrese el nombre exacto del equipo a prestar: ")
        if nombre not in self.inventario:
            print("El equipo no existe.")
            return

        equipo = self.inventario[nombre]

        if not equipo.esta_disponible():
            print(f"Error: El equipo '{nombre}' no esta disponible.")
            return

        usuario = input("Ingrese el nombre del usuario: ")
        fecha = input("Ingrese la fecha del prestamo (DD/MM/AAAA): ")

        equipo.prestar(usuario, fecha)
        print(f"Prestamo registrado: '{nombre}' fue prestado a {usuario} el {fecha}.")

    def devolver_equipo(self):
        print("\nDevolver Equipo")
        nombre = input("Ingrese el nombre exacto del equipo a devolver: ")

        if nombre not in self.inventario:
            print("Error: El equipo no existe en el sistema.")
            return

        equipo = self.inventario[nombre]

        if equipo.esta_disponible():
            print(f"El equipo '{nombre}' ya estaba disponible.")
            return

        equipo.devolver()
        print(f"Equipo '{nombre}' devuelto correctamente.")

    def ver_historial(self):
        print("\nHistorial de Prestamos")
        for equipo in self.inventario.values():
            print(f"\n{equipo.nombre}:")
            if equipo.prestamos:
                for prestamo in equipo.prestamos:
                    print(f"  {prestamo}")
            else:
                print("  Sin prestamos registrados.")

    def agregar_equipo(self):
        print("\nAgregar Nuevo Equipo")
        nombre = input("Ingrese el nombre del nuevo equipo: ")

        if nombre in self.inventario:
            print("Error: El equipo ya existe en el sistema.")
            return

        self.inventario[nombre] = Equipo(nombre)
        print(f"Equipo '{nombre}' registrado exitosamente.")

    def menu(self):
        while True:
            print("\nSistema de Prestamos de Equipos")
            print("1. Ver equipos disponibles")
            print("2. Registrar prestamo")
            print("3. Devolver equipo")
            print("4. Ver historial de prestamos")
            print("5. Agregar nuevo equipo")
            print("6. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.mostrar_equipos()
            elif opcion == "2":
                self.registrar_prestamo()
            elif opcion == "3":
                self.devolver_equipo()
            elif opcion == "4":
                self.ver_historial()
            elif opcion == "5":
                self.agregar_equipo()
            elif opcion == "6":
                print("Saliendo...")
                break
            else:
                print("Opcion no valida.")


if __name__ == "__main__":
    sistema = SistemaPrestamos()
    sistema.menu()
