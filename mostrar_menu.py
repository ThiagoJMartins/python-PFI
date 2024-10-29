# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu(colors):
    # Limpiar la pantalla
    print("\033c", end="")

    # Mostrar el menú
    print(f"{colors.CYAN}+----------------------------------+{colors.RESET}")
    print(f"{colors.CYAN}|           {colors.BOLD}Menú principal{colors.RESET}         {colors.CYAN}|{colors.RESET}")
    print(f"{colors.CYAN}+----------------------------------+{colors.RESET}")
    print(f"{colors.GREEN}| 1. Agregar un producto           |{colors.RESET}")
    print(f"{colors.GREEN}| 2. Mostrar los productos         |{colors.RESET}")
    print(f"{colors.GREEN}| 0. Salir                         |{colors.RESET}")
    print(f"{colors.CYAN}+----------------------------------+{colors.RESET}")

    # Solicitar la opción del usuario
    while True:
        opcion = int(input(f"\n{colors.YELLOW}Seleccioná una opción: {colors.RESET}"))
        if opcion in [0, 1, 2]:
            return opcion
        else:
            print(f"{colors.YELLOW}Opción no válida. Intentá nuevamente.{colors.RESET}")
