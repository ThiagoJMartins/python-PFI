# Función para agregar un producto al inventario
def agregar_producto(inventario, colors):
    while True:
        # Limpiar la pantalla
        print("\033c", end="")

        # Mostrar encabezado del menú
        print(f"{colors.CYAN}+---------------------------------+{colors.RESET}")
        print(f"{colors.CYAN}|    {colors.BOLD}Alta de productos nuevos{colors.RESET}     {colors.CYAN}|{colors.RESET}")
        print(f"{colors.CYAN}+---------------------------------+{colors.RESET}")

        # Solicitar los datos del producto
        nombre = input(f"{colors.GREEN}Ingresá el nombre del producto: {colors.RESET}")
        cantidad = int(input(f"{colors.GREEN}Ingresá la cantidad del producto: {colors.RESET}"))
        precio = float(input(f"{colors.GREEN}Ingresá el precio del producto: {colors.RESET}"))

        # Agregar el producto a la lista
        inventario.append([nombre, cantidad, precio])
        
        # Mostrar un mensaje de éxito
        print(f"\n{colors.YELLOW}Producto '{nombre}' agregado con éxito.{colors.RESET}")

        while True:
            # Solicitar opción al usuario
            opcion = input(f"\n{colors.CYAN}¿Deseás agregar otro producto? (s/n): {colors.RESET}")

            if opcion.lower() == "s":
                break  # Salir del bucle interno para agregar otro producto
            elif opcion.lower() == "n":
                return
            else:
                print(f"\n{colors.YELLOW}Opción no válida. Intentá nuevamente.{colors.RESET}")
