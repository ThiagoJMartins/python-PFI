import mostrar_menu as menu
import agregar_producto as agregar
import mostrar_productos as mostrar
import colors

# Lista para almacenar los productos
inventario = []

# Bucle principal del menú interactivo
while True:
    opcion = menu.mostrar_menu(colors)
    
    if opcion == 1:
        agregar.agregar_producto(inventario, colors)
    elif opcion == 2:
        mostrar.mostrar_productos(inventario, colors)
    elif opcion == 0:
        print(f"\n{colors.RED}Saliendo del programa...{colors.RESET}\n")
        break
    else:
        print(f"{colors.YELLOW}Opción no válida. Intentá nuevamente.{colors.RESET}")
