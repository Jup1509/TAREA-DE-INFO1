#Ejercicio en esta dipositiva:
# Definición de funciones para las operaciones entre conjuntos
def union_conjuntos(A, B):
    resultado = A.union(B)
    print(f"\nUnión (A ∪ B): {resultado}")


def interseccion_conjuntos(A, B):
    resultado = A.intersection(B)
    print(f"\nIntersección (A ∩ B): {resultado}")


def diferencia_conjuntos(A, B):
    resultado_A_B = A.difference(B)
    resultado_B_A = B.difference(A)
    print(f"\nDiferencia (A - B): {resultado_A_B}")
    print(f"Diferencia (B - A): {resultado_B_A}")


def diferencia_simetrica_conjuntos(A, B):
    resultado = A.symmetric_difference(B)
    print(f"\nDiferencia simétrica (A Δ B): {resultado}")


# Diccionario con las funciones asociadas a claves
operaciones = {
    '1': union_conjuntos,
    '2': interseccion_conjuntos,
    '3': diferencia_conjuntos,
    '4': diferencia_simetrica_conjuntos,
}


def ingresar_conjunto(nombre):
    """Solicita y valida el ingreso de números flotantes a un conjunto."""
    conjunto = set()
    print(f"\n--- Ingreso de elementos para el Conjunto {nombre} ---")

    while True:
        entrada = input(
            f"Ingrese un número flotante para el Conjunto {nombre} (o escriba 'fin' para terminar): "
        ).strip()

        if entrada.lower() == 'fin':
            break

        try:
            numero = float(entrada)
            conjunto.add(numero)
            print(f"Número {numero} agregado con éxito.")
        except ValueError:
            print("Error: Debe ingresar un número flotante válido.")

    return conjunto


def menu_operaciones():
    # Inicialización de conjuntos vacíos
    A = set()
    B = set()

    # Carga de datos
    A = ingresar_conjunto("A")
    B = ingresar_conjunto("B")

    print(f"\nConjunto A final: {A}")
    print(f"Conjunto B final: {B}")

    while True:
        print("\n--- MENÚ DE OPERACIONES DE CONJUNTOS ---")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Diferencia simétrica")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == '5':
            print("Saliendo del programa...")
            break
        elif opcion in operaciones:
            # Ejecución de la función almacenada en el diccionario
            operaciones[opcion](A, B)
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el programa
menu_operaciones()