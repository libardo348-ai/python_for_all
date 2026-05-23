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
#declara las clascificacion de compromiso según la duración y los clics de la sesión. Si la duración es mayor a 180 segundos y los clics son mayores a 8, se clasifica como "Alto". Si la duración es menor a 60 segundos o los clics son menores a 3, se clasifica como "Bajo". En cualquier otro caso, se clasifica como "Medio".
def generar_informe(sesiones):
    #Genera e imprime un informe con el ID de cliente y su clasificación."""
    print("Informe de compromiso de sesiones")
    print("--------------------------------")
    for sesion in sesiones:
        cliente_id, duracion, clics = sesion
        nivel = clasificar_compromiso(duracion, clics)
        print(f"Cliente {cliente_id}: {nivel}")
#Genera un informe que muestra el ID de cada cliente junto con su nivel de compromiso (Alto, Medio o Bajo) basado en la duración y los clics de cada sesión. El informe se imprime en la consola con un formato claro y organizado.
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
#imprime mensaje de error si el usuario ingresa un número fuera del rango permitido o un valor no numérico. Continúa solicitando la cantidad de sesiones hasta que se ingrese un valor válido.
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
#imprime mensajes de error específicos para cada tipo de entrada inválida: si el ID del cliente no 
# es alfanumérico, 
# si la duración o los clics no son números enteros positivos. Continúa solicitando los datos
#  de la sesión hasta que se ingresen valores válidos.
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

#solicita confirmacion para imprimir el informe, aceptando respuestas como "SI", "S", "NO" o "N" 
# (en mayúsculas o minúsculas). Si la respuesta es afirmativa, devuelve True; si es negativa, devuelve False. 
# Si la respuesta no es válida, solicita al usuario que responda nuevamente hasta que se ingrese una respuesta correcta.
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
#imprime un mensaje de error si ocurre algún problema al intentar guardar el historial en el archivo. 
# Si el guardado es exitoso, confirma al usuario que el historial ha sido guardado correctamente.

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
        #ofrece al usuario tres opciones claras para gestionar los registros de sesiones: 
        # guardar y cerrar, guardar y continuar,
        #  o descartar y cerrar. Cada opción incluye una descripción detallada de lo que implica, ayudando al usuario a tomar u
        # na decisión informada sobre cómo proceder con los datos ingresados. El programa continúa solicitando una opción válida
        #  hasta que el usuario seleccione una de las opciones disponibles.
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

#seleccion de opciones de gestión de registros, donde el usuario puede elegir entre 
# guardar y cerrar, guardar y continuar o descartar y cerrar.
if __name__ == "__main__":
    sesiones = pedir_sesiones()
    if solicitar_impresion_informe():
        generar_informe(sesiones)
        #Este bloque comprueba que el programa se está ejecutando directamente,
        #  y no se está usando como parte de otro código importado.
    else:
        print("✓ Informe no impreso. Podrá guardar o descartar los datos a continuación.")
    gestionar_registros(sesiones)
#el programa indica que el informe no se imprimirá si el usuario decide no imprimirlo, pero le recuerda que aún puede gestionar 
# los registros ingresados a través de las opciones disponibles.
