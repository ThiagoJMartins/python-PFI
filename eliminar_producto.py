def eliminar_producto(inventario, colors):
    while True:
        # Limpiar la pantalla
        print("\033c", end="")

        # Mostrar encabezado del menú
        print(f"{colors.RED}╔" + "═" * 85 + f"╗{colors.RESET}")
        print(f"{colors.RED}║{colors.RESET} {colors.BOLD}{'Eliminar un producto':^83}{colors.RESET} {colors.RED}║{colors.RESET}")
        print(f"{colors.RED}╠" + "═" * 85 + f"╣{colors.RESET}")

       # Verificar si el inventario está vacío
        if not inventario:
            print(f"\n{colors.YELLOW}No hay productos en el inventario para actualizar.{colors.RESET}\n")
            input(f"{colors.YELLOW}Presioná 'Enter' para regresar al menú...{colors.RESET}")
            return

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

       # Solicitar el código del producto a eliminar
        try:
            codigo = input(f"\n{colors.YELLOW}Ingresá el código del producto a eliminar: {colors.RESET}").strip()

            # Buscar y eliminar producto por código
            producto_eliminado = None
            for idx, producto in enumerate(inventario):
                if producto[0] == codigo:
                    producto_eliminado = inventario.pop(idx)
                    break

            if producto_eliminado:
                print(f"\n{colors.RED}Producto '{colors.BOLD}{producto_eliminado[1]}{colors.RESET}{colors.RED}' eliminado con éxito.{colors.RESET}")
            else:
                print(f"\n{colors.RED}Error: Código no encontrado. Intentá nuevamente.{colors.RESET}")

        except ValueError:
            print(f"\n{colors.RED}Error: Debés ingresar un número válido.{colors.RESET}")
        
        # Preguntar si desea eliminar otro producto
        while True:
            opcion = input(f"\n{colors.CYAN}¿Deseás eliminar otro producto? (s/n): {colors.RESET}").strip().lower()
            if opcion == "s":
                break
            elif opcion == "n":
                print(f"\n{colors.YELLOW}Regresando al menú principal...{colors.RESET}")
                return
            else:
                print(f"{colors.RED}Opción no válida. Ingresá 's' o 'n'.{colors.RESET}")