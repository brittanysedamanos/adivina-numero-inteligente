# -*- coding: utf-8 -*-
"""
MODULO: Interfaz de usuario - Version mejorada
"""

import math

def mostrar_bienvenida(configuracion):
    """Mostrar pantalla de bienvenida al juego."""
    print("=" * 50)
    print("        ADIVINA EL NUMERO - SISTEMA INTELIGENTE")
    print("=" * 50)
    print("\nDIFICULTAD: " + configuracion['dificultad'].upper())
    print("RANGO: " + str(configuracion['min_valor']) + " - " + str(configuracion['max_valor']))
    print("\nDESCRIPCION:")
    print("Este sistema usa algoritmos matematicos avanzados")
    print("para adivinar el numero en que estas pensando.")
    print("\nINSTRUCCIONES:")
    print("1. Piensa en un numero secreto")
    print("2. Responde honestamente a cada intento")
    print("3. Observa como el algoritmo es eficiente")
    
    # Obtener nombre del jugador
    nombre = ""
    while not nombre:
        nombre = raw_input("\nIngresa tu nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacio. Intenta nuevamente.")
    
    return nombre

def mostrar_despedida(nombre_jugador, total_intentos, configuracion):
    """Mostrar mensaje de despedida con estadisticas."""
    print("\n" + "=" * 50)
    print("            RESUMEN DE LA PARTIDA")
    print("=" * 50)
    print("\nJUGADOR: " + nombre_jugador)
    print("DIFICULTAD: " + configuracion['dificultad'].upper())
    print("RANGO: " + str(configuracion['min_valor']) + "-" + str(configuracion['max_valor']))
    print("INTENTOS TOTALES: " + str(total_intentos))
    
    # Calcular eficiencia
    import math
    rango_total = float(configuracion["max_valor"] - configuracion["min_valor"] + 1)
    max_teorico = int(math.ceil(math.log(rango_total) / math.log(2)))
    
    if total_intentos > 0 and max_teorico > 0:
        eficiencia = ((max_teorico - total_intentos) / float(max_teorico)) * 100
        eficiencia_final = max(eficiencia, 0)
        print("EFICIENCIA DEL ALGORITMO: %.1f%%" % eficiencia_final)
        
        # Mensaje personalizado segun eficiencia
        if eficiencia_final >= 80:
            print("\n¡EXCELENTE! El algoritmo fue super eficiente.")
        elif eficiencia_final >= 60:
            print("\n¡MUY BIEN! El algoritmo funciono como se esperaba.")
        elif eficiencia_final >= 40:
            print("\n¡BUEN INTENTO! El algoritmo tuvo que esforzarse mas.")
        else:
            print("\n¿Hubo algun cambio en el numero durante el juego?")
    else:
        print("\nNo se pudo calcular la eficiencia.")
    
    print("\n" + "=" * 50)
