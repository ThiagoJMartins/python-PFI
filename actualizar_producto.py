def actualizar_producto(inventario, colors):
    while True:
        # Limpiar la pantalla
        print("\033c", end="")

        # Mostrar encabezado
        print(f"{colors.BLUE}╔" + "═" * 85 + f"╗{colors.RESET}")
        print(f"{colors.BLUE}║{colors.RESET} {colors.BOLD}{'Actualizar un producto':^83}{colors.RESET} {colors.BLUE}║{colors.RESET}")
        print(f"{colors.BLUE}╠" + "═" * 85 + f"╣{colors.RESET}")

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

        # Solicitar el código del producto a actualizar
        codigo = input(f"\n{colors.YELLOW}Ingresá el código del producto a actualizar: {colors.RESET}").strip()

        # Validar código
        for producto in inventario:
            if producto[0] == codigo:
                print(f"\n{colors.CYAN}Actualizando producto: '{producto[1]}'{colors.RESET}")

                # Menú de campos a actualizar
                while True:
                    print(f"""\n{colors.GREEN}¿Qué campo deseás actualizar?
1. Nombre
2. Descripción
3. Cantidad
4. Precio
5. Categoría
0. Finalizar actualización{colors.RESET}""")
                    try:
                        opcion = int(input(f"{colors.YELLOW}Seleccioná una opción: {colors.RESET}").strip())
                        if opcion == 1:
                            nuevo_nombre = input(f"{colors.GREEN}Ingresá el nuevo nombre: {colors.RESET}").strip()
                            producto[1] = nuevo_nombre
                        elif opcion == 2:
                            nueva_descripcion = input(f"{colors.GREEN}Ingresá la nueva descripción: {colors.RESET}").strip()
                            producto[2] = nueva_descripcion
                        elif opcion == 3:
                            nueva_cantidad = int(input(f"{colors.GREEN}Ingresá la nueva cantidad: {colors.RESET}").strip())
                            producto[3] = nueva_cantidad
                        elif opcion == 4:
                            nuevo_precio = float(input(f"{colors.GREEN}Ingresá el nuevo precio: {colors.RESET}").strip())
                            producto[4] = nuevo_precio
                        elif opcion == 5:
                            nueva_categoria = input(f"{colors.GREEN}Ingresá la nueva categoría: {colors.RESET}").strip()
                            producto[5] = nueva_categoria
                        elif opcion == 0:
                            print(f"\n{colors.YELLOW}Actualización finalizada. Regresando al menú principal...{colors.RESET}")
                            return
                        else:
                            print(f"\n{colors.RED}Error: Opción no válida. Intentá nuevamente.{colors.RESET}")
                    except ValueError:
                        print(f"\n{colors.RED}Error: Debés ingresar un número válido.{colors.RESET}")
                break
        else:
            print(f"\n{colors.RED}Error: Código no encontrado. Intentá nuevamente.{colors.RESET}")

        # Preguntar si desea actualizar otro producto
        while True:
            opcion = input(f"\n{colors.CYAN}¿Deseás actualizar otro producto? (s/n): {colors.RESET}").strip().lower()
            if opcion == "s":
                break
            elif opcion == "n":
                print(f"\n{colors.YELLOW}Regresando al menú principal...{colors.RESET}")
                return
            else:
                print(f"{colors.RED}Opción no válida. Ingresá 's' o 'n'.{colors.RESET}")
