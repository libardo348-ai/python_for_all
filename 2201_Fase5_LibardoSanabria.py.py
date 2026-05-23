
#LIBARDO SANABRIA HERNANDEZ
#FUNDAMENTOS DE PROGRAMACION
#2201

def clasificar_compromiso(duracion, clics):
    #Calcula la clasificación de compromiso según duración y eventos de clic."""
    if duracion > 180 and clics > 8:
        return "Alto"
    if duracion < 60 or clics < 3:
        return "Bajo"
    return "Medio"

def generar_informe(sesiones):
    #Genera e imprime un informe con el ID de cliente y su clasificación."""
    print("Informe de compromiso de sesiones")
    print("--------------------------------")
    for sesion in sesiones:
        cliente_id, duracion, clics = sesion
        nivel = clasificar_compromiso(duracion, clics)
        print(f"Cliente {cliente_id}: {nivel}")

def pedir_sesiones():
    #Pregunta cuántas sesiones desea ingresar (1 a 5) y devuelve la matriz resultante."""
    max_sesiones = 5
    while True:
        try:
            cantidad = int(input(f"¿Cuántas sesiones desea ingresar? (1-{max_sesiones}): "))
            if cantidad < 1 or cantidad > max_sesiones:
                print(f"  ⚠ Error: ingrese un número entre 1 y {max_sesiones}.")
                continue
            break
        except ValueError:
            print("  ⚠ Error: Ingrese solo números enteros válidos.")

    sesiones = []
    for i in range(1, cantidad + 1):
        print(f"\nSesión {i} de {cantidad}")
        while True:
            try:
                cliente_id = input("  ID Cliente (alfanumérico): ").strip()
                duracion = int(input("  Duración (segundos): "))
                clics = int(input("  Eventos Clics: "))

                if not cliente_id or not cliente_id.isalnum():
                    print("  ⚠ Error: ID debe ser alfanumérico, sin espacios ni símbolos.")
                    continue
                if duracion <= 0 or clics <= 0:
                    print("  ⚠ Error: Ingrese números positivos mayores a 0.")
                    continue

                sesiones.append([cliente_id, duracion, clics])
                break
            except ValueError:
                print("  ⚠ Error: Ingrese solo números enteros válidos para duración y clics.")

    return sesiones


def solicitar_impresion_informe():
    #Pregunta al usuario si desea imprimir el informe y devuelve True/False.
    while True:
        respuesta = input("¿Desea imprimir el informe? (SI/NO): ").strip().lower()
        if respuesta in ["si", "s"]:
            return True
        if respuesta in ["no", "n"]:
            return False
        print("Por favor responda SI o NO.")


def guardar_historial(sesiones):
    #Guarda los registros de sesiones en un archivo de historial.
    try:
        with open("historial_sesiones.txt", "a") as archivo:
            archivo.write("\n--- Sesiones Guardadas ---\n")
            for sesion in sesiones:
                cliente_id, duracion, clics = sesion
                nivel = clasificar_compromiso(duracion, clics)
                archivo.write(f"Cliente {cliente_id}: Duración={duracion}s, Clics={clics}, Nivel={nivel}\n")
        print("✓ Historial guardado en 'historial_sesiones.txt'")
    except Exception as e:
        print(f"Error al guardar el historial: {e}")


def gestionar_registros(sesiones):
    #Ofrece opciones para guardar, continuar o descartar la sesión.
    while True:
        print("\n" + "="*70)
        print("¿QUÉ DESEA HACER?")
        print("="*70)
        print("\n1. Guardar y cerrar")
        print("   ✓ Guarda todo en 'historial_sesiones.txt'")
        print("   ✓ Cierra el programa")
        
        print("\n2. Guardar y continuar")
        print("   ✓ Guarda todo en 'historial_sesiones.txt'")
        print("   ✓ Permite ingresar más sesiones")
        
        print("\n3. Descartar y cerrar")
        print("   ✗ NO guarda nada")
        print("   ✗ Cierra el programa y pierde todos los datos")
        
        print("="*70)
        opcion = input("Seleccione una opción (1/2/3): ").strip()
        
        if opcion == "1":
            guardar_historial(sesiones)
            print("\n✓ Datos guardados correctamente")
            print("¡Programa finalizado!")
            break
            
        elif opcion == "2":
            guardar_historial(sesiones)
            print("\n✓ Datos guardados correctamente")
            print("Ingrese más sesiones...\n")
            nuevas_sesiones = pedir_sesiones()
            sesiones.extend(nuevas_sesiones)
            if solicitar_impresion_informe():
                generar_informe(sesiones)
            else:
                print("✓ Informe no impreso.")
                
        elif opcion == "3":
            print("\n✗ Datos descartados")
            print("¡Programa finalizado!")
            break
                
        else:
            print("❌ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    sesiones = pedir_sesiones()
    if solicitar_impresion_informe():
        generar_informe(sesiones)
    else:
        print("✓ Informe no impreso. Podrá guardar o descartar los datos a continuación.")
    gestionar_registros(sesiones)
