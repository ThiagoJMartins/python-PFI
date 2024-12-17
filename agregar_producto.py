# Función para agregar un producto al inventario
def agregar_producto(inventario, colors):
    while True:
        # Limpiar la pantalla
        print("\033c", end="")

        # Encabezado del menú
        print(f"{colors.CYAN}╔" + "═" * 45 + f"╗{colors.RESET}")
        print(f"{colors.CYAN}║{colors.RESET} {colors.BOLD}{'Alta de productos nuevos':^43}{colors.RESET} {colors.CYAN}║{colors.RESET}")
        print(f"{colors.CYAN}╚" + "═" * 45 + f"╝{colors.RESET}")

        try:
            # Solicitar el código único del producto
            while True:
                codigo = input(f"{colors.GREEN}Código único del producto : {colors.RESET}").strip()
                if not codigo:
                    print(f"{colors.RED}Error: El código no puede estar vacío.{colors.RESET}")
                elif any(producto[0] == codigo for producto in inventario):
                    print(f"{colors.RED}Error: El código '{codigo}' ya existe. Ingresá un código único.{colors.RESET}")
                else:
                    break

            # Solicitar los demás datos del producto
            print(f"{colors.CYAN}┌" + "─" * 45 + f"┐{colors.RESET}")
            nombre = input(f"{colors.GREEN}Nombre del producto       : {colors.RESET}").strip()
            descripcion = input(f"{colors.GREEN}Descripción del producto  : {colors.RESET}").strip()
            cantidad = int(input(f"{colors.GREEN}Cantidad                  : {colors.RESET}").strip())
            precio = float(input(f"{colors.GREEN}Precio                    : {colors.RESET}").strip())
            categoria = input(f"{colors.GREEN}Categoría                 : {colors.RESET}").strip()
            print(f"{colors.CYAN}└" + "─" * 45 + f"┘{colors.RESET}")

            # Validar campos vacíos
            if not nombre or not descripcion or not categoria:
                print(f"\n{colors.RED}Error: Todos los campos deben completarse.{colors.RESET}")
                input(f"{colors.YELLOW}Presioná 'Enter' para intentarlo de nuevo...{colors.RESET}")
                continue

            # Agregar el producto a la lista
            inventario.append([codigo, nombre, descripcion, cantidad, precio, categoria])

            # Mensaje de éxito
            print(f"\n{colors.YELLOW}¡Producto '{colors.BOLD}{nombre}{colors.RESET}{colors.YELLOW}' agregado con éxito!{colors.RESET}")

        except ValueError:
            print(f"\n{colors.RED}Error: Ingresaste un valor inválido. Asegurate de completar los campos correctamente.{colors.RESET}")
            input(f"{colors.YELLOW}Presioná 'Enter' para intentarlo de nuevo...{colors.RESET}")
            continue

        # Confirmación para agregar otro producto
        while True:
            opcion = input(f"\n{colors.CYAN}¿Deseás agregar otro producto? (s/n): {colors.RESET}").strip().lower()
            if opcion == "s":
                break  # Volver al inicio del bucle
            elif opcion == "n":
                print(f"\n{colors.YELLOW}Regresando al menú principal...{colors.RESET}")
                return  # Salir de la función
            else:
                print(f"{colors.RED}Opción no válida. Ingresá 's' o 'n'.{colors.RESET}")
