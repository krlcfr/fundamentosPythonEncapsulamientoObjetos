inventario = {
    "Laptop HP": {"disponible": True, "prestamos": []},
    "Monitor Dell": {"disponible": True, "prestamos": []},
    "Teclado Logitech": {"disponible": True, "prestamos": []},
    "Mouse inalambrico": {"disponible": True, "prestamos": []},
}


def mostrar_equipos():
    print("\nEquipos en el sistema")
    for nombre, datos in inventario.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"{nombre} - {estado}")


def registrar_prestamo():
    print("\nRegistrar Prestamo")
    mostrar_equipos()
    equipo = input("\nIngrese el nombre exacto del equipo a prestar: ")
    if equipo not in inventario:
        print("El equipo no existe.")
        return
    if not inventario[equipo]["disponible"]:
        print(f"Error: El equipo '{equipo}' no esta disponible.")
        return
    usuario = input("Ingrese el nombre del usuario: ")
    fecha = input("Ingrese la fecha del prestamo (DD/MM/AAAA): ")
    prestamo = (usuario, fecha)
    inventario[equipo]["prestamos"].append(prestamo)
    inventario[equipo]["disponible"] = False
    print(f"Prestamo registrado: '{equipo}' fue prestado a {usuario} el {fecha}.")


def devolver_equipo():
    print("\nDevolver Equipo")
    equipo = input("Ingrese el nombre exacto del equipo a devolver: ")
    if equipo not in inventario:
        print("Error: El equipo no existe en el sistema.")
        return
    if inventario[equipo]["disponible"]:
        print(f"El equipo '{equipo}' ya estaba disponible.")
        return
    inventario[equipo]["disponible"] = True
    print(f"Equipo '{equipo}' devuelto correctamente.")


def ver_historial():
    print("\nHistorial de Prestamos")
    for nombre, datos in inventario.items():
        print(f"\n{nombre}:")
        if datos["prestamos"]:
            for prestamo in datos["prestamos"]:
                print(f"  Usuario: {prestamo[0]}, Fecha: {prestamo[1]}")
        else:
            print("  Sin prestamos registrados.")


def agregar_equipo():
    print("\nAgregar Nuevo Equipo")
    nombre = input("Ingrese el nombre del nuevo equipo: ")
    if nombre in inventario:
        print("Error: El equipo ya existe en el sistema.")
        return
    inventario[nombre] = {"disponible": True, "prestamos": []}
    print(f"Equipo '{nombre}' registrado exitosamente.")


def menu():
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
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
