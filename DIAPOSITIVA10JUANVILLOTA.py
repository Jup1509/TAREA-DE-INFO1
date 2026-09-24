#Ejercicio calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def menu_calculadora():
    while True:
        print("\n--- MENU CALCULADORA ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "5":
            print("Saliendo de la calculadora...")
            break
        elif opcion in ["1", "2", "3", "4"]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == "1":
                print(f"Resultado: {sumar(num1, num2)}")
            elif opcion == "2":
                print(f"Resultado: {restar(num1, num2)}")
            elif opcion == "3":
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcion == "4":
                print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar
menu_calculadora()

#Ejercicio teorema del seno y coseno
import math

def calcular_lado_coseno(a, b, C_deg):
    C_rad = math.radians(C_deg)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C_rad))
    return c

def calcular_angulo_seno(a, c, C_deg):
    C_rad = math.radians(C_deg)
    sin_A = (a * math.sin(C_rad)) / c
    sin_A = max(-1.0, min(1.0, sin_A)) # Prevenir errores de precisión
    A_rad = math.asin(sin_A)
    return math.degrees(A_rad)

def resolver_lal(a, b, C_deg):
    c = calcular_lado_coseno(a, b, C_deg)
    A_deg = calcular_angulo_seno(a, c, C_deg)
    B_deg = 180 - A_deg - C_deg
    return c, A_deg, B_deg

def resolver_ala(A_deg, c, B_deg):
    C_deg = 180 - A_deg - B_deg
    A_rad = math.radians(A_deg)
    B_rad = math.radians(B_deg)
    C_rad = math.radians(C_deg)
    
    a = (c * math.sin(A_rad)) / math.sin(C_rad)
    b = (c * math.sin(B_rad)) / math.sin(C_rad)
    return a, b, C_deg

def menu_triangulo():
    print("\n--- RESOLUCIÓN DE TRIÁNGULOS ---")
    print("1. Lado - Ángulo - Lado (LAL)")
    print("2. Ángulo - Lado - Ángulo (ALA)")
    opcion = input("Seleccione el caso conocido (1 o 2): ")
    
    if opcion == "1":
        a = float(input("Ingrese lado a: "))
        b = float(input("Ingrese lado b: "))
        C = float(input("Ingrese el ángulo C comprendido entre a y b (en grados): "))
        c, A, B = resolver_lal(a, b, C)
        print(f"\nResultados:\n Lado c = {c:.2f}\n Ángulo A = {A:.2f}°\n Ángulo B = {B:.2f}°")
    elif opcion == "2":
        A = float(input("Ingrese el ángulo A (en grados): "))
        c = float(input("Ingrese el lado c adyacente a A y B: "))
        B = float(input("Ingrese el ángulo B (en grados): "))
        a, b, C = resolver_ala(A, c, B)
        print(f"\nResultados:\n Lado a = {a:.2f}\n Lado b = {b:.2f}\n Ángulo C = {C:.2f}°")
    else:
        print("Opción no válida.")

# Ejecutar
menu_triangulo()

#Ejercicio de historia clínica
from datetime import datetime

def crear_paciente():
    nombre = input("Nombre completo: ")
    identificacion = input("Número de identificación: ")
    fecha_str = input("Fecha de nacimiento (DD/MM/AAAA): ")
    fecha_nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y")
    edad = int(input("Edad: "))
    eps = input("EPS: ")
    
    # Tupla con datos del paciente
    return (identificacion, nombre, fecha_nacimiento, edad, eps)

def almacenar_paciente(base_datos, paciente):
    base_datos.append(paciente)

def buscar_paciente(base_datos, identificacion):
    # Uso del operador 'in' para verificar presencia por ID
    ids_almacenados = [p[0] for p in base_datos]
    if identificacion in ids_almacenados:
        for p in base_datos:
            if p[0] == identificacion:
                print(f"\n--- PACIENTE ENCONTRADO ---")
                print(f"ID: {p[0]}\nNombre: {p[1]}\nFecha Nacimiento: {p[2].strftime('%d/%m/%Y')}\nEdad: {p[3]}\nEPS: {p[4]}")
                return
    else:
        print("\nEl paciente no se encuentra en la base de datos.")

def menu_hce():
    base_datos = []  # Lista vacía
    while True:
        print("\n--- HISTORIA CLÍNICA ELECTRÓNICA ---")
        print("1. Ingresar nuevo paciente")
        print("2. Buscar paciente por ID")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            paciente = crear_paciente()
            almacenar_paciente(base_datos, paciente)
            print("Paciente registrado con éxito.")
        elif opcion == "2":
            id_buscar = input("Ingrese el ID a buscar: ")
            buscar_paciente(base_datos, id_buscar)
        elif opcion == "3":
            print("\n--- BASE DE DATOS FINAL ---")
            for p in base_datos:
                print(f"ID: {p[0]} | Nombre: {p[1]} | Nacimiento: {p[2].strftime('%d/%m/%Y')} | Edad: {p[3]} | EPS: {p[4]}")
            break
        else:
            print("Opción inválida.")

# Ejecutar
menu_hce()

#Ejercicio calendario
def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

def dias_en_mes(mes, año):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(año) else 28
    return 0

def calcular_dia_siguiente(dia, mes, año):
    max_dias = dias_en_mes(mes, año)
    
    if dia < max_dias:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            año += 1
        else:
            mes += 1
            
    return dia, mes, año

def menu_calendario():
    while True:
        print("\n--- CALCULAR DÍA SIGUIENTE ---")
        fecha_input = input("Ingrese la fecha (dd, mm, aaaa o dd/mm/aaaa): ")
        
        # Limpieza de entrada
        separador = "," if "," in fecha_input else "/"
        partes = [int(p.strip()) for p in fecha_input.split(separador)]
        dia, mes, año = partes[0], partes[1], partes[2]
        
        d, m, a = calcular_dia_siguiente(dia, mes, año)
        
        print(f"La fecha ingresada es bisiesta?: {'Sí' if es_bisiesto(año) else 'No'}")
        print(f"El día siguiente es: {d:02d}/{m:02d}/{a}")
        
        continuar = input("\n¿Desea hallar otra fecha? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saliendo del programa...")
            break

# Ejecutar
menu_calendario()