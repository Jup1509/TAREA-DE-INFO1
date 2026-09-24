#Ejercicio calculadora optimizada
# Operaciones aritméticas definidas como funciones lambda
sumar = lambda a, b: a + b
restar = lambda a, b: a - b
multiplicar = lambda a, b: a * b
dividir = lambda a, b: a / b

def solicitar_numero(mensaje):
    """Función auxiliar para validar que el ingreso sea un número entero o flotante."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("\nERROR - Ingresó un dato incorrecto. Intente de nuevo.\n")

def calculadora_optimizada():
    while True:
        print("\n--- MENÚ CALCULADORA OPTIMIZADA ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "5":
            print("Saliendo de la calculadora...")
            break
        elif opcion in ["1", "2", "3", "4"]:
            num1 = solicitar_numero("Ingrese el primer número: ")
            num2 = solicitar_numero("Ingrese el segundo número: ")
            
            try:
                if opcion == "1":
                    resultado = sumar(num1, num2)
                elif opcion == "2":
                    resultado = restar(num1, num2)
                elif opcion == "3":
                    resultado = multiplicar(num1, num2)
                elif opcion == "4":
                    if num2 == 0:
                        raise ZeroDivisionError
                    resultado = dividir(num1, num2)
                
                print(f"Resultado: {resultado}")
                
            except ZeroDivisionError:
                print("\nERROR - división por cero. Intente de nuevo.\n")
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
calculadora_optimizada()