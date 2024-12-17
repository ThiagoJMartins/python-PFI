# Función para mostrar los productos en el inventario
def mostrar_productos(inventario, colors):
    # Limpiar la pantalla
    print("\033c", end="")

    # Mostrar los productos en el inventario
    if not inventario:
        print(f"\n{colors.YELLOW}No hay productos en el inventario.{colors.RESET}\n")
    else:
        # Encabezado de la tabla
        print(f"{colors.CYAN}╔" + "═" * 85 + f"╗{colors.RESET}")
        print(f"{colors.CYAN}║{colors.RESET} {colors.BOLD}{'Listado de Productos':^83}{colors.RESET} {colors.CYAN}║{colors.RESET}")
        print(f"{colors.CYAN}╠" + "═" * 85 + f"╣{colors.RESET}")

        # Columnas
        print(f"{colors.CYAN}║ {colors.BOLD}{'Código':^10}│{'Nombre':^14}│{'Descripción':^18}│{'Cantidad':^10}│{'Precio':^10}│{'Categoría':^16}{colors.RESET} {colors.CYAN}║{colors.RESET}")
        print(f"{colors.CYAN}╠" + "─" * 11 + "┼" + "─" * 14 + "┼" + "─" * 18 + "┼" + "─" * 10 + "┼" + "─" * 10 + "┼" + "─" * 17 + f"╣{colors.RESET}")

        # Filas de productos
        for producto in inventario:
            codigo, nombre, descripcion, cantidad, precio, categoria = producto

            # Truncar valores largos para mantener las columnas ordenadas
            nombre_truncado = (nombre[:12] + '..') if len(nombre) > 14 else nombre
            descripcion_truncada = (descripcion[:16] + '..') if len(descripcion) > 18 else descripcion
            categoria_truncada = (categoria[:15] + '..') if len(categoria) > 17 else categoria

            # Formatear las columnas y centrar el código
            codigo_centrado = str(codigo).center(10)

            # Mostrar cada producto en una fila
            print(f"{colors.CYAN}║{colors.RESET}{colors.GREEN} {codigo_centrado}│{nombre_truncado:<14}│{descripcion_truncada:<18}│{cantidad:>10}│{precio:>10.2f}│{categoria_truncada:<16} {colors.CYAN}║{colors.RESET}")


        # Pie de tabla
        print(f"{colors.CYAN}╚" + "═" * 85 + f"╝{colors.RESET}")

    # Esperar a que el usuario presione 'Enter'
    while True:
        opcion = input(f"\n{colors.YELLOW}Presioná 'Enter' para continuar...{colors.RESET}")
        if opcion == "":
            break
        else:
            print(f"\n{colors.RED}Opción no válida. Intentá nuevamente.{colors.RESET}")
