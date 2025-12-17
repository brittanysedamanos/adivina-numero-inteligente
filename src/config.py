# -*- coding: utf-8 -*-
"""
MODULO: Configuracion y estadisticas del juego
"""

import json
import os

CONFIG_FILE = "config.json"
STATS_FILE = "estadisticas.json"

def inicializar():
    """Inicializa los archivos de configuracion si no existen."""
    if not os.path.exists(CONFIG_FILE):
        configuracion_default = {
            "dificultad": "normal",
            "min_valor": 1,
            "max_valor": 100,
            "max_intentos": 15
        }
        guardar_configuracion(configuracion_default)
    
    if not os.path.exists(STATS_FILE):
        with open(STATS_FILE, 'w') as f:
            json.dump({}, f)

def obtener_configuracion():
    """Obtiene la configuracion actual del juego."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except:
        # Configuracion por defecto si hay error
        return {
            "dificultad": "normal",
            "min_valor": 1,
            "max_valor": 100,
            "max_intentos": 15
        }

def guardar_configuracion(configuracion):
    """Guarda la configuracion en el archivo."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(configuracion, f, indent=4)

def menu_configuracion_dificultad():
    """Menu interactivo para configurar la dificultad."""
    import utils
    
    utils.limpiar_pantalla()
    print("=" * 50)
    print("        CONFIGURACION DE DIFICULTAD")
    print("=" * 50)
    
    print("\nSelecciona el nivel de dificultad:")
    print("\n1. FACIL (Numeros del 1 al 50)")
    print("2. NORMAL (Numeros del 1 al 100)")
    print("3. DIFICIL (Numeros del 1 al 200)")
    print("4. EXPERTO (Numeros del 1 al 500)")
    print("5. PERSONALIZADO (Elige tu propio rango)")
    print("6. VOLVER AL MENU PRINCIPAL")
    print("\n" + "=" * 50)
    
    while True:
        try:
            opcion = int(raw_input("\nSeleccion (1-6): "))
            
            if opcion == 1:
                nueva_config = {
                    "dificultad": "facil",
                    "min_valor": 1,
                    "max_valor": 50,
                    "max_intentos": 10
                }
                guardar_configuracion(nueva_config)
                print("\nConfiguracion guardada: Dificultad FACIL (1-50)")
                raw_input("Presiona ENTER para continuar...")
                return
                
            elif opcion == 2:
                nueva_config = {
                    "dificultad": "normal",
                    "min_valor": 1,
                    "max_valor": 100,
                    "max_intentos": 15
                }
                guardar_configuracion(nueva_config)
                print("\nConfiguracion guardada: Dificultad NORMAL (1-100)")
                raw_input("Presiona ENTER para continuar...")
                return
                
            elif opcion == 3:
                nueva_config = {
                    "dificultad": "dificil",
                    "min_valor": 1,
                    "max_valor": 200,
                    "max_intentos": 20
                }
                guardar_configuracion(nueva_config)
                print("\nConfiguracion guardada: Dificultad DIFICIL (1-200)")
                raw_input("Presiona ENTER para continuar...")
                return
                
            elif opcion == 4:
                nueva_config = {
                    "dificultad": "experto",
                    "min_valor": 1,
                    "max_valor": 500,
                    "max_intentos": 25
                }
                guardar_configuracion(nueva_config)
                print("\nConfiguracion guardada: Dificultad EXPERTO (1-500)")
                raw_input("Presiona ENTER para continuar...")
                return
                
            elif opcion == 5:
                print("\nCONFIGURACION PERSONALIZADA")
                print("-" * 30)
                
                try:
                    min_valor = int(raw_input("Valor minimo: "))
                    max_valor = int(raw_input("Valor maximo: "))
                    
                    if min_valor >= max_valor:
                        print("Error: El valor minimo debe ser menor al maximo.")
                        continue
                    
                    nueva_config = {
                        "dificultad": "personalizado",
                        "min_valor": min_valor,
                        "max_valor": max_valor,
                        "max_intentos": 30
                    }
                    guardar_configuracion(nueva_config)
                    print("\nConfiguracion guardada: Rango " + str(min_valor) + "-" + str(max_valor))
                    raw_input("Presiona ENTER para continuar...")
                    return
                    
                except ValueError:
                    print("Error: Debes ingresar numeros validos.")
                    
            elif opcion == 6:
                return
                
            else:
                print("Opcion invalida. Ingresa un numero entre 1 y 6.")
                
        except ValueError:
            print("Error: Debes ingresar un numero.")

def guardar_estadistica(nombre_jugador, intentos):
    """Guarda una estadistica de partida."""
    try:
        with open(STATS_FILE, 'r') as f:
            estadisticas = json.load(f)
    except:
        estadisticas = {}
    
    # Agregar nueva estadistica
    clave = nombre_jugador + "_" + str(len(estadisticas) + 1)
    estadisticas[clave] = intentos
    
    # Mantener solo las ultimas 20 estadisticas
    if len(estadisticas) > 20:
        # Convertir a lista, tomar ultimos 20, volver a diccionario
        items = list(estadisticas.items())[-20:]
        estadisticas = dict(items)
    
    with open(STATS_FILE, 'w') as f:
        json.dump(estadisticas, f, indent=4)

def obtener_estadisticas():
    """Obtiene todas las estadisticas guardadas."""
    try:
        with open(STATS_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}
