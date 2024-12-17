# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu(colors):
    while True:
        # Limpiar la pantalla
        print("\033c", end="")

        # Encabezado del menú
        print(f"{colors.CYAN}╔" + "═" * 34 + f"╗{colors.RESET}")
        print(f"{colors.CYAN}║{colors.RESET} {colors.BOLD}{'Menú Principal':^32}{colors.RESET} {colors.CYAN}║{colors.RESET}")
        print(f"{colors.CYAN}╚" + "═" * 34 + f"╝{colors.RESET}")

        # Opciones del menú
        print(f"{colors.GREEN}╭──────────────────────────────────╮{colors.RESET}")
        print(f"{colors.GREEN}│ {colors.BOLD}1.{colors.RESET} Agregar un producto           {colors.GREEN}│{colors.RESET}")
        print(f"{colors.GREEN}│ {colors.BOLD}2.{colors.RESET} Mostrar los productos         {colors.GREEN}│{colors.RESET}")
        print(f"{colors.GREEN}│ {colors.BOLD}3.{colors.RESET} Actualizar un producto        {colors.GREEN}│{colors.RESET}")
        print(f"{colors.GREEN}│ {colors.BOLD}4.{colors.RESET} Eliminar un producto          {colors.GREEN}│{colors.RESET}")
        print(f"{colors.GREEN}│ {colors.BOLD}5.{colors.RESET} Buscar un producto            {colors.GREEN}│{colors.RESET}")
        print(f"{colors.GREEN}│ {colors.BOLD}0.{colors.RESET} Salir                         {colors.GREEN}│{colors.RESET}")
        print(f"{colors.GREEN}╰──────────────────────────────────╯{colors.RESET}")

        # Solicitar la opción del usuario
        try:
            opcion = int(input(f"\n{colors.YELLOW}Seleccioná una opción: {colors.RESET}").strip())
            if opcion in [0, 1, 2, 3, 4, 5]:
                return opcion
            else:
                print(f"\n{colors.RED}Error: Opción incorrecta. Ingrese un índice válido.{colors.RESET}")
        except ValueError:
            print(f"\n{colors.RED}Error: Debés ingresar un número válido.{colors.RESET}")

        input(f"\n{colors.YELLOW}Presioná 'Enter' para intentarlo nuevamente...{colors.RESET}")
