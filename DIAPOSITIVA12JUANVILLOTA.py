#Ejercicio de facturación e inventario de productos
# Diccionarios de artículos segun las especificaciones
camisetas = {
    1: ['Polo', 'Blanca', 15],
    2: ['Polo', 'Azul', 15],
    3: ['Polo', 'Roja', 15],
    4: ['Polo', 'Amarilla', 15],
    5: ['Cuello redondo', 'Gris', 12],
    6: ['Cuello redondo', 'Negro', 12],
    7: ['Cuello redondo', 'Verde', 12]
}

jean = {
    1: ['Azul', 20],
    2: ['Verde', 20],
    3: ['Café', 20],
    4: ['Negro', 20],
    5: ['Gris', 20]
}

zapatos = {
    1: ['Botas', 'Café', 25],
    2: ['Tenis', 'Azul', 20],
    3: ['Botas', 'Negro', 25],
    4: ['Tenis', 'Blanco', 20]
}


def solicitar_numero(mensaje):
    """Valida que el ingreso sea estrictamente numérico entero."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("\nError: Debe ingresar SOLO números. Intente nuevamente.\n")


def seleccionar_opcion_diccionario(diccionario, nombre_categoria):
    """Permite seleccionar una clave válida de un diccionario con manejo de excepciones."""
    print(f"\n--- Opciones de {nombre_categoria} ---")
    for clave, valor in diccionario.items():
        print(f"{clave}. {valor}")

    while True:
        try:
            opcion = int(
                input(f"Seleccione el número de {nombre_categoria}: ")
            )
            if opcion in diccionario:
                return diccionario[opcion]
            else:
                print("Error: La opción ingresada no está en el catálogo.")
        except ValueError:
            print("\nError: Debe ingresar SOLO números. Intente nuevamente.\n")


def facturar_compra():
    while True:
        print("\n========================================")
        print("      SISTEMA DE FACTURACIÓN Y TIENDA")
        print("========================================")

        # Captura de datos del comprador
        nombre = input("Nombre y apellido del comprador: ").strip()
        identificacion = solicitar_numero("Número de identificación: ")
        direccion = input("Dirección: ").strip()
        telefono = solicitar_numero("Teléfono: ")

        # Lista vacía para almacenar los 3 artículos seleccionados
        compra = []

        print("\n--- SELECCIÓN DE 3 ARTÍCULOS ---")

        # Artículo 1: Camiseta
        item_camiseta = seleccionar_opcion_diccionario(camisetas, "Camiseta")
        compra.append({
            'categoria': 'Camiseta',
            'detalle': f"{item_camiseta[0]} {item_camiseta[1]}",
            'precio': item_camiseta[2]
        })

        # Artículo 2: Jean
        item_jean = seleccionar_opcion_diccionario(jean, "Jean")
        compra.append({
            'categoria': 'Jean',
            'detalle': f"Color {item_jean[0]}",
            'precio': item_jean[1]
        })

        # Artículo 3: Zapatos
        item_zapatos = seleccionar_opcion_diccionario(zapatos, "Zapatos")
        compra.append({
            'categoria': 'Zapatos',
            'detalle': f"{item_zapatos[0]} {item_zapatos[1]}",
            'precio': item_zapatos[2]
        })

        # Imprimir Factura Final
        total = 0
        print("\n" + "=" * 45)
        print("             FACTURA DE COMPRA")
        print("=" * 45)
        print(f"Cliente: {nombre}")
        print(f"ID: {identificacion}")
        print(f"Dirección: {direccion}")
        print(f"Teléfono: {telefono}")
        print("-" * 45)
        print("Artículos comprados:")

        for i, item in enumerate(compra, 1):
            print(
                f"{i}. {item['categoria']} ({item['detalle']}) - ${item['precio']}"
            )
            total += item['precio']

        print("-" * 45)
        print(f"TOTAL A PAGAR: ${total}")
        print("=" * 45)

        # Preguntar si desea realizar otra compra o salir
        opcion_salida = (
            input("\n¿Desea hacer otra compra? (s/n): ").strip().lower()
        )
        if opcion_salida != 's':
            print("\n¡Gracias por su compra! Saliendo del programa...")
            break


# Ejecutar el programa
facturar_compra()