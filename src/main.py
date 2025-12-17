# -*- coding: utf-8 -*-
"""
PROYECTO FINAL: ADIVINA EL NUMERO - SISTEMA INTELIGENTE
VERSION PROFESIONAL CON MENUS, NIVELES Y REINICIO
ESTUDIANTE: Brittany Jhulisa Sedamanos León
FECHA: 17 de diciembre de 2025
"""

import juego
import interfaz
import utils
import config

def mostrar_menu_principal():
    """Muestra el menu principal del juego."""
    utils.limpiar_pantalla()
    print("=" * 50)
    print("       ADIVINA EL NUMERO - MENU PRINCIPAL")
    print("=" * 50)
    print("\n1. JUGAR NUEVA PARTIDA")
    print("2. CONFIGURAR DIFICULTAD")
    print("3. VER ESTADISTICAS")
    print("4. AYUDA / INSTRUCCIONES")
    print("5. SALIR DEL JUEGO")
    print("\n" + "=" * 50)
    
    while True:
        try:
            opcion = int(raw_input("\nSelecciona una opcion (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Opcion invalida. Por favor ingresa un numero entre 1 y 5.")
        except ValueError:
            print("Error: Debes ingresar un numero valido.")

def jugar_partida():
    """Ejecuta una partida completa del juego."""
    # Obtener configuracion actual
    configuracion = config.obtener_configuracion()
    
    # Mostrar bienvenida y obtener nombre
    nombre_jugador = interfaz.mostrar_bienvenida(configuracion)
    
    # Crear juego con la configuracion actual
    juego_actual = juego.JuegoAdivinanza(nombre_jugador, configuracion)
    
    # Iniciar juego
    juego_actual.iniciar()
    
    # Guardar estadisticas
    config.guardar_estadistica(nombre_jugador, juego_actual.intentos)
    
    # Mostrar despedida
    interfaz.mostrar_despedida(nombre_jugador, juego_actual.intentos, configuracion)
    
    # Preguntar si quiere jugar otra vez
    return preguntar_reinicio()

def preguntar_reinicio():
    """Pregunta al usuario si quiere jugar otra partida."""
    print("\n" + "=" * 50)
    print("          ¿QUE QUIERES HACER AHORA?")
    print("=" * 50)
    print("\n1. JUGAR OTRA PARTIDA")
    print("2. VOLVER AL MENU PRINCIPAL")
    print("3. SALIR DEL JUEGO")
    print("\n" + "=" * 50)
    
    while True:
        try:
            opcion = int(raw_input("\nSelecciona una opcion (1-3): "))
            if 1 <= opcion <= 3:
                return opcion
            else:
                print("Opcion invalida. Ingresa 1, 2 o 3.")
        except ValueError:
            print("Error: Ingresa un numero valido.")

def mostrar_estadisticas():
    """Muestra las estadisticas de partidas anteriores."""
    utils.limpiar_pantalla()
    print("=" * 50)
    print("          ESTADISTICAS DEL JUEGO")
    print("=" * 50)
    
    estadisticas = config.obtener_estadisticas()
    
    if not estadisticas:
        print("\nNo hay estadisticas registradas aun.")
        print("¡Juega algunas partidas para generar estadisticas!")
    else:
        print("\nRESUMEN DE PARTIDAS:")
        print("-" * 40)
        
        total_partidas = len(estadisticas)
        total_intentos = sum(estadisticas.values())
        promedio = total_intentos / float(total_partidas) if total_partidas > 0 else 0
        
        print("Total de partidas jugadas: " + str(total_partidas))
        print("Promedio de intentos por partida: %.1f" % promedio)
        
        # Mostrar las ultimas 5 partidas
        print("\nULTIMAS PARTIDAS:")
        print("-" * 40)
        items = list(estadisticas.items())
        for i, (jugador, intentos) in enumerate(items[-5:], 1):
            print(str(i) + ". " + jugador + ": " + str(intentos) + " intentos")
    
    print("\n" + "=" * 50)
    raw_input("\nPresiona ENTER para volver al menu...")

def mostrar_ayuda():
    """Muestra las instrucciones del juego."""
    utils.limpiar_pantalla()
    print("=" * 50)
    print("          AYUDA E INSTRUCCIONES")
    print("=" * 50)
    
    print("\nCOMO JUGAR:")
    print("1. Piensa en un numero secreto")
    print("2. La computadora intentara adivinarlo")
    print("3. Responde honestamente a cada intento:")
    print("   - 1 si tu numero es MENOR")
    print("   - 2 si tu numero es MAYOR")
    print("   - 3 si adivino CORRECTAMENTE")
    
    print("\nALGORITMO UTILIZADO:")
    print("- Busqueda binaria (divide y venceras)")
    print("- Siempre elige el numero del medio")
    print("- Maxima eficiencia: O(log n)")
    
    print("\nNIVELES DE DIFICULTAD:")
    print("- Facil: Numeros del 1 al 50")
    print("- Normal: Numeros del 1 al 100")
    print("- Dificil: Numeros del 1 al 200")
    print("- Experto: Numeros del 1 al 500")
    print("- Personalizado: Tu eliges el rango")
    
    print("\nCONSEJOS:")
    print("- No cambies tu numero durante el juego")
    print("- Responde honestamente para mejores resultados")
    print("- Observa como el algoritmo se hace mas preciso")
    
    print("\n" + "=" * 50)
    raw_input("\nPresiona ENTER para volver al menu...")

def main():
    """Funcion principal del programa."""
    # Inicializar configuracion
    config.inicializar()
    
    ejecutando = True
    
    while ejecutando:
        opcion = mostrar_menu_principal()
        
        if opcion == 1:  # Jugar nueva partida
            resultado = jugar_partida()
            
            if resultado == 1:  # Jugar otra
                continue
            elif resultado == 2:  # Volver al menu
                continue
            else:  # Salir
                ejecutando = False
                
        elif opcion == 2:  # Configurar dificultad
            config.menu_configuracion_dificultad()
            
        elif opcion == 3:  # Ver estadisticas
            mostrar_estadisticas()
            
        elif opcion == 4:  # Ayuda
            mostrar_ayuda()
            
        elif opcion == 5:  # Salir
            print("\nGracias por jugar ADIVINA EL NUMERO.")
            print("¡Hasta la proxima!")
            ejecutando = False
    
    print("\nPrograma terminado.")

if __name__ == "__main__":
    main()
