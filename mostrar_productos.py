# Función para mostrar los productos en el inventario
def mostrar_productos(inventario, colors):
    # Limpiar la pantalla
    print("\033c", end="")

    # Mostrar los productos en el inventario
    if not inventario:
        print(f"\n{colors.YELLOW}No hay productos en el inventario.{colors.RESET}\n")
    else:
        print(f"{colors.CYAN}+--------------------------------------+{colors.RESET}")
        print(f"{colors.CYAN}|         {colors.BOLD}Listado de productos{colors.RESET}         {colors.CYAN}|{colors.RESET}")
        print(f"{colors.CYAN}+--------------------------------------+{colors.RESET}")
        print(f"{colors.CYAN}| {'Nombre':^10} | {'Cantidad':^10} | {'Precio':^10} |{colors.RESET}")
        print(f"{colors.CYAN}|" + "-" * 38 + f"|{colors.RESET}")
        
        for producto in inventario:
            # Limitar el nombre del producto a 10 caracteres
            nombre_truncado = (producto[0][:7] + '...') if len(producto[0]) > 10 else producto[0]
            print(f"{colors.GREEN}| {nombre_truncado:<10} | {producto[1]:^10} | {producto[2]:>10.2f} |{colors.RESET}")
        
        print(f"{colors.CYAN}+" + "-" * 38 + f"+{colors.RESET}")

    # Esperar a que el usuario presione 'Enter'
    while True:
        opcion = input(f"\n{colors.YELLOW}Presioná 'Enter' para continuar...{colors.RESET}")
        if opcion == "":
            break
        else:
            print(f"\n{colors.YELLOW}Opción no válida. Intentá nuevamente.{colors.RESET}")